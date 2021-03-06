# -*- coding: utf-8 -*-
import scrapy
from .. items import BookInfo


class IntroSpider(scrapy.Spider):
    name = 'intro'
    allowed_domains = ['jjwxc.net']
    start_urls = ['http://www.jjwxc.net/onebook.php?novelid=3141967']

    def parse(self, response):
        intro = BookInfo()

        sel = response.css('[name=Author]')
        intro['author'] = sel.xpath('@content').extract_first()
        # u"《(.*)》"
        # 《张公案2》大风刮过_【原创小说|纯爱小说】_晋江文学城
        intro['book_title'] = response.xpath(
            '/html/head/title/text()').re_first(u'《(.*)》.*')
        intro['short_intro'] = response.css(
            '[id=novelintro]::text').extract()

        yield intro
