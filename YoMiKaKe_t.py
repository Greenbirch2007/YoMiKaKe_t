#! -*- coding:utf-8 -*-
import datetime
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver
import pyautogui

import datetime
import re
import string
import time


# 读取页面文本
# 按照标题，保存整个文本





import csv
import datetime

import os
import re
import time
import sys
import xlrd
import pymysql
import xlrd
import requests
from requests.exceptions import RequestException
from lxml import etree
import  pandas  as pd

import pymysql

import csv
import datetime
import numpy as np


import os
import re
import time
import sys

sys.getfilesystemencoding()
import pymysql
import xlrd






def writerDt_csv(headers, rowsdata):
    # rowsdata列表中的数据元组,也可以是字典数据
    with open('sc_jsIndex.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # # if 去掉表头
    # if rowNum > 0:

    return dataFile
driver = webdriver.Chrome()

















def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='YMKK',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:


        cursor.executemany('insert into YoMiKaKe (hanzi,jiaming,hanyi,type_) values (%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    big_list = []



    data = pd.read_excel("w_t.xlsx")
    data = data.values
    for item in data.tolist():
        url_c = item[0].split()
        type_= item[1]
        url = 'https://www.google.com/search?q={0}%E8%AA%AD%E3%81%BF%E6%96%B9&sxsrf=ALeKk01KgDYV6ZdYnechx5GNGg77oIq9FQ%3A1621933275104&ei=27ysYL_5Ba6Ur7wPqruu-Ac&oq=Crontab%E8%AA%AD%E3%81%BF%E6%96%B9&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHlD57wFY-e8BYKP2AWgAcAB4AIAB6AOIAY0FkgEHMC4xLjQtMZgBAKABAqABAaoBB2d3cy13aXrAAQE&sclient=gws-wiz&ved=0ahUKEwj_0tilvOTwAhUuyosBHaqdC38Q4dUDCA4&uact=5'.format(url_c[0])
        driver.get(url)
        html = driver.page_source
        patt = re.compile('<span data-dobid="hdw">(.*?)</span>' + '.*?<span lang="zh-CN">(.*?)</span>')
        item_x = re.findall(patt, html)
        if item != None:
            try:


                f_content = url_c[0],item_x[0][0],item_x[0][1][2:-2],item[1]
                print(f_content)
                insertDB([f_content])
            except:
                pass

        else:
            pass












#
# create table YoMiKaKe
# (id int not null primary key auto_increment,
# hanzi text,
# jiaming text,
# hanyi text,
# type_ text)
# engine=InnoDB  charset=utf8;


# drop  table YoMiKaKe;
