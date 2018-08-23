# -*- coding: utf-8 -*-
import subprocess
import time
import os
import sys
import xml.etree.ElementTree as ET


def sort_children(parent, attr):
    parent[:] = sorted(parent, key=lambda child: child.get(attr))


def output_txt_from_content_xml(input, output):
    tree = ET.parse(input)
    root = tree.getroot()

    item_num = 1
    order = {}

    for item in root.findall('item'):
        item_index = item.find('index').text
        if not item_index.isdigit():
            root.remove(item)
        else:
            order[item_index] = item_num
            item_num += 1

    with open(output, 'a') as ff:
        for ii in range(1, item_num):
            ff.write("\n")
            title = root.find('.//item[%d]/title' % order[str(ii)]).text
            ff.write(title.encode("GBK") + "\n\n")
            content_list = root.findall(
                './/item[%d]/content/value' % order[str(ii)])
            for paragraph in content_list:
                para_content = paragraph.text
                if para_content is not None:
                    para_content = para_content
                    ff.write(para_content.encode("GBK") + "\n")
            ff.write("\n")
            talk = root.find('.//item[%d]/talk' % order[str(ii)]).text
            if talk != "None":
                ff.write(talk.encode("GBK") + "\n\n")


def output_txt_from_intro_xml(input, output):
    tree = ET.parse(input)
    root = tree.getroot()

    with open(output, 'w') as ff:
        title = root.find('.//book_title').text
        line = u"《" + title + u"》\n\n"
        ff.write(line.encode("GBK"))
        author = root.find('.//author').text
        line = u"作者：" + author + "\n\n"
        ff.write(line.encode("GBK"))
        line = u"文案：\n"
        ff.write(line.encode("GBK"))
        value_list = root.findall('.//item/short_intro/value')
        for value in value_list:
            line = "    " + value.text
            if line is not None:
                ff.write(line.encode("GBK") + "\n")
        ff.write("\n")


def copy_template_to_spider(template, spider, mode):
    spider_file = open(spider, mode)

    with open(template, 'r') as ff:
        code_buffer = ff.read()
        spider_file.write(code_buffer)

    spider_file.close()


def add_book_num_to_spider(spider, book_number):
    with open(spider, 'a') as ff:
        ff.write(book_number)


def modify_spider(book_number):
    spider_path = "jjbooks/spiders/book.py"

    copy_template_to_spider("spider_template_part1.txt", spider_path, "w")
    add_book_num_to_spider(spider_path, book_number)
    copy_template_to_spider("spider_template_part2.txt", spider_path, "a")

    intro_spider_path = "jjbooks/spiders/intro.py"
    copy_template_to_spider(
        "intro_spider_template_part1.txt", intro_spider_path, "w")
    add_book_num_to_spider(intro_spider_path, book_number)
    copy_template_to_spider(
        "intro_spider_template_part2.txt", intro_spider_path, "a")


if (__name__ == "__main__"):
    # usage: python get.py 3141967
    # https://wap.jjwxc.net/book2/3435320?more=0&whole=1
    # print "Book number: %s" % sys.argv[1]
    book_number = sys.argv[1]
    modify_spider(book_number)

    tt = time.localtime()
    txt_filename = "output%s.txt" % time.strftime("%m%d", tt)
    intro_filename = "intro%s.xml" % time.strftime("%m%d", tt)
    content_filename = "test%s.xml" % time.strftime("%m%d", tt)

    if os.path.exists(intro_filename):
        os.remove(intro_filename)

    if os.path.exists(content_filename):
        os.remove(content_filename)

    cmd = "scrapy crawl intro -o %s --nolog" % intro_filename
    subprocess.call(cmd)
    cmd = "scrapy crawl book -o %s --nolog" % content_filename
    subprocess.call(cmd)

    output_txt_from_intro_xml(intro_filename, txt_filename)
    output_txt_from_content_xml(content_filename, txt_filename)
