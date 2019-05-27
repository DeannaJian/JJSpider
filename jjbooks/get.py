# -*- coding: utf-8 -*-
import subprocess
import time
import os
import sys
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle


def login_and_get_cookie(username, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://wap.jjwxc.net/my/login?login_mode=jjwxc')
    driver.implicitly_wait(10)
    usr = driver.find_element_by_xpath("//*[@id='loginname']")
    usr.clear()
    usr.send_keys(username)
    psw = driver.find_element_by_xpath("//*[@id='loginpass']")
    psw.send_keys(password)
    sub = driver.find_element_by_xpath("//*[@name='sub']")
    sub.click()

    new_cookie = {}
    for item in driver.get_cookies():
        new_cookie.setdefault(
            item["name"].encode('utf-8'),
            item["value"].encode('utf-8'))

    driver.close()

    with open('current_cookie.pkl', 'wb') as ff:
        pickle.dump(new_cookie, ff)


def sort_children(parent, attr):
    parent[:] = sorted(parent, key=lambda child: child.get(attr))


def output_txt_from_content_xml(input_file, output_file):
    tree = ET.parse(input_file)
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

    with open(output_file, 'a', encoding="utf-8") as ff:
        for ii in range(1, item_num):
            ff.write("\n")
            title = root.find('.//item[%d]/title' % order[str(ii)]).text
            ff.write(title + "\n\n")
            content_list = root.findall(
                './/item[%d]/content/value' % order[str(ii)])
            for paragraph in content_list:
                para_content = paragraph.text
                if para_content is not None:
                    para_content = para_content
                    ff.write(para_content + "\n")
            ff.write("\n")
            talk_list = root.find('.//item[%d]/talk' % order[str(ii)])
            for paragraph in talk_list:
                para_content = paragraph.text
                if para_content is not None:
                    ff.write(para_content + "\n")
            ff.write("\n")


def get_author_title_from_intro_xml(input_file):
    tree = ET.parse(input_file)
    root = tree.getroot()

    title = root.find('.//book_title').text
    author = root.find('.//author').text
    return title, author


def standardized_filename(filename):
    forbidden_character = ('\\', '/', ':', '*', '?', '"', '<', '>', '|')
    for cc in forbidden_character:
        filename = filename.replace(cc, ' ')
    return filename


def get_txt_filename(intro_file):
    title, author = get_author_title_from_intro_xml(intro_file)
    title = standardized_filename(title)
    output_filename = u"《" + title + u"》_" + author + '.txt'
    return output_filename


def output_txt_from_intro_xml(input_file, output_file):
    title, author = get_author_title_from_intro_xml(input_file)

    tree = ET.parse(input_file)
    root = tree.getroot()

    with open(output_file, 'w', encoding="utf-8") as ff:
        line = u"《" + title + u"》\n\n"
        ff.write(line)
        line = u"作者：" + author + "\n\n"
        ff.write(line)
        line = u"文案：\n"
        ff.write(line)
        value_list = root.findall('.//item/short_intro/value')
        for value in value_list:
            line = value.text
            if line is not None:
                ff.write(line + "\n")
        ff.write("\n")


def output_txt(input_file, output_file, output_type):
    assert(output_type in ("intro", "content"))

    if output_type == "intro":
        output_txt_from_intro_xml(input_file, output_file)
    else:
        output_txt_from_content_xml(input_file, output_file)


def copy_template_to_spider(template, spider, mode):
    spider_file = open(spider, mode=mode, encoding='utf-8', errors='ignore')

    with open(template, 'r', encoding='utf-8', errors='ignore') as ff:
        code_buffer = ff.read()
        spider_file.write(code_buffer)

    spider_file.close()


def add_book_num_to_spider(spider, book_number):
    with open(spider, 'a') as ff:
        ff.write(book_number)


def modify_spider(book_number, spider_type):
    assert(spider_type in ("intro", "content"))

    spider_path = "jjbooks/spiders/intro.py" if (spider_type == "intro") \
        else "jjbooks/spiders/book.py"
    template_name = "intro_spider_template_part" if (spider_type == "intro") \
        else "spider_template_part"

    copy_template_to_spider(template_name + "1.txt", spider_path, "w")
    add_book_num_to_spider(spider_path, book_number)
    copy_template_to_spider(template_name + "2.txt", spider_path, "a")


def get_intro(book_number, output_folder, txt_filename):
    modify_spider(book_number, "intro")

    tt = time.localtime()
    temp_filename = "temp_output%s.xml" % time.strftime("%m%d", tt)

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    cmd = "scrapy crawl intro -o %s --nolog" % temp_filename
    subprocess.call(cmd)

    txt_filename = output_folder + "\\" + get_txt_filename(temp_filename)
    output_txt_from_intro_xml(temp_filename, txt_filename)
    os.remove(temp_filename)

    return txt_filename


def get_content(book_number, output_folder, txt_filename):
    modify_spider(book_number, "content")

    tt = time.localtime()
    temp_filename = "temp_output%s.xml" % time.strftime("%m%d", tt)

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    cmd = "scrapy crawl book -o %s --nolog" % temp_filename
    subprocess.call(cmd)

    output_txt_from_content_xml(temp_filename, txt_filename)
    os.remove(temp_filename)


def get_book_part(book_number, output_folder, output_type, txt_filename):
    assert(output_type in ("intro", "content"))
    modify_spider(book_number, output_type)
    spider_name = "intro" if (output_type == "intro") else "book"

    tt = time.localtime()
    temp_filename = "temp_output%s.xml" % time.strftime("%m%d", tt)

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    cmd = "scrapy crawl %s -o %s --nolog" % (spider_name, temp_filename)
    subprocess.call(cmd)

    if (output_type == "intro"):
        txt_filename = output_folder + "\\" + get_txt_filename(temp_filename)
        output_txt_from_intro_xml(temp_filename, txt_filename)
    else:
        output_txt_from_content_xml(temp_filename, txt_filename)

    os.remove(temp_filename)

    return txt_filename


def get_book(book_number, output_folder, refresh_cookie, username, password):
    if refresh_cookie:
        login_and_get_cookie(username, password)

    txt_filename = get_book_part(book_number, output_folder, "intro", "")
    get_book_part(book_number, output_folder, "content", txt_filename)


if (__name__ == "__main__"):
    # usage: python get.py 3141967
    # if cookie has to be refresh, use: python get.py 3141967 username passwd
    # https://wap.jjwxc.net/book2/3435320?more=0&whole=1
    # print "Book number: %s" % sys.argv[1]

    if len(sys.argv) == 5:
        number = sys.argv[2]
        folder = sys.argv[1]
        get_book(number, folder, True, sys.argv[3], sys.argv[4])
    elif len(sys.argv) == 3:
        number = sys.argv[2]
        folder = sys.argv[1]
        get_book(number, folder, False, "dummy", "dummy")
    else:
        print('''
usage:
    python get.py output_folder book_number
example:
    python get.py "c:\\temp" 3141967

if cookie has to be refresh, use:
    python get.py 3141967 username passwd
            ''')
