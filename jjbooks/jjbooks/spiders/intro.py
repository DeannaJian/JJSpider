# -*- coding: utf-8 -*-
import scrapy
from .. items import BookInfo
from selenium import webdriver
from lxml import etree
import re
from selenium.webdriver.chrome.options import Options


class IntroSpider(scrapy.Spider):
    name = 'intro'
    allowed_domains = ['wap.jjwxc.net']
    start_urls = ['https://wap.jjwxc.net/book2/3886659?more=0&whole=1']

    def __init__(self):
        scrapy.Spider.__init__(self)
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(10)
        html = etree.HTML(self.driver.page_source)
        links = html.xpath('//*[@href]')
        attrib_dict = links[6].attrib

        intro = BookInfo()
        intro['author'] = response.xpath(
            '/html/head/title/text()').re_first(u'.*》(.*)_【.*')
        intro['book_title'] = response.xpath(
            '/html/head/title/text()').re_first(u'《(.*)》.*')
        intro_list = response.css('[id=novelintro]::text').extract()
        if 'onclick' in attrib_dict:
            pattern = re.compile(r'showMore\(\'(.*)\'\)')
            intro_appended = pattern.match(links[6].attrib['onclick']).group(1)
            intro_appended = intro_appended.replace('<br />', '\n')            
            intro_text = intro_list[1] + intro_appended
            intro['short_intro'] = [intro_text]
        else:
            intro['short_intro'] = intro_list

        self.driver.close()

        yield intro
