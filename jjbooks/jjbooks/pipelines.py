# -*- coding: utf-8 -*-
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JjbooksPipeline(object):
    def process_item(self, item, spider):
        base_dir = os.getcwd()
        filename = base_dir + "/output.txt"
        with open(filename, 'a') as f:
            title = item['title']
            content = item['content']
            talk = item['talk']
            f.write(title.encode("gb2312") + '\n\n')
            for ii in content:
                f.write(ii.encode("gb2312") + '\n')
            f.write(talk.encode("gb2312") + '\n\n\n\n')
        return item
