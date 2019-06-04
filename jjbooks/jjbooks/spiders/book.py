# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from .. items import ChapterItem


class BookSpider(scrapy.Spider):
    import pickle
    import os

    cookie = {}
    if os.path.exists('current_cookie.pkl'):
        with open('current_cookie.pkl', 'rb') as ff:
            cookie = pickle.load(ff)

    name = 'book'
    allowed_domains = ['wap.jjwxc.net']
    start_urls = ['https://wap.jjwxc.net/book2/3886659?more=0&whole=1']

    headers = {
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 \
        Safari/537.36'
    }

    def start_requests(self):
        # self.response_index = 1
        return [scrapy.Request(
            self.start_urls[0],
            cookies=self.cookie, callback=self.parse,
            headers=self.headers)]

    def parse(self, response):
        le = LinkExtractor(restrict_css='[style="text-decoration:none"]')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, cookies=self.cookie,
                                 callback=self.parse_chapter)

    def parse_chapter(self, response):
        chapter = ChapterItem()

        chapter['title'] = response.css('h2::text').extract_first()

        chapter['talk'] = (response.css(
            '[style="font-size: 12px; color: #009900;"]::text')
            .extract())

        chapter['content'] = (response.css(
            '[style="line-height: 25.2px"]::text').extract())

        chapter['index'] = response.css('h2::text').re_first('\d+')

        yield chapter
