# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChapterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    talk = scrapy.Field()
    index = scrapy.Field()


class BookInfo(scrapy.Item):
    book_title = scrapy.Field()
    author = scrapy.Field()
    short_intro = scrapy.Field()
