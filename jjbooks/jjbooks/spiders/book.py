# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from .. items import ChapterItem
from scrapy.conf import settings


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['wap.jjwxc.net']
    start_urls = ['https://wap.jjwxc.net/book2/3435320?more=0&whole=1']

    cookie = settings['COOKIE']  # 带着Cookie向网页发请求

    # 发送给服务器的http头信息，有的网站需要伪装出浏览器头进行爬取，有的则不需要
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }

    # 对请求的返回进行处理的配置
    meta = {
        'dont_redirect': True,  # 禁止网页重定向
        'handle_httpstatus_list': [301, 302]  # 对哪些异常返回进行处理
    }

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], callback=self.parse,
                             cookies=self.cookie,
                             headers=self.headers, meta=self.meta)

    def parse(self, response):
        le = LinkExtractor(restrict_css='[style="text-decoration:none"]')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_chapter)

    def parse_chapter(self, response):
        chapter = ChapterItem()

        chapter['title'] = response.css('h2::text').extract_first()

        chapter['talk'] = (response.css(
            '[style="font-size: 12px; color: #009900;"]::text')
            .extract_first())

        chapter['content'] = (response.css(
            '[style="line-height: 25.2px"]::text').extract())

        chapter['index'] = response.css('h2::text').re_first('\d+')

        yield chapter
