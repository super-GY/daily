#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"

import pymysql
import xlrd

# 连接数据库
try:
    db = pymysql.connect(host="127.0.0.1",
                         port=3306,
                         user="root",
                         passwd="123456",
                         db="lang",
                         charset='utf8')
except:
    print("could not connect to mysql server")


def open_excel():
    try:
        book = xlrd.open_workbook("lang2020-05-29.xls")  # 文件名，把文件与py文件放在同一目录下
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("Sheet1")  # execl里面的worksheet1
        return sheet
    except:
        print("locate worksheet in excel failed!")


def insert_data():
    sheet = open_excel()
    cursor = db.cursor()
    row_num = sheet.nrows
    for i in range(1, row_num):  # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        row_data = sheet.row_values(i)
        value = (row_data[0], row_data[1], row_data[2], row_data[3])
        value = list(value)
        # import time
        # tupTime = time.localtime(value[3])  # 秒时间戳
        # stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
        # print(stadardTime)
        # value[2] = stadardTime
        # value[2] = str(value[2])

        print(value)
        sql = """insert into lang_banner(id, image, link_url, is_active) values (%s,%s,%s,%s)"""
        # sql = """insert into goods_banner(id, image, add_time, goods_id, index) values (%s,%s,%s,%s,%s)"""

        cursor.execute(sql, value)  # 执行sql语句

        db.commit()
    cursor.close()  # 关闭连接


open_excel()
insert_data()

"""
遇到问题：
pymysql.err.ProgrammingError: (1064, "You have an error in your SQL syntax; check the manual that corresponds to 
your MySQL server version for the right syntax to use near 'index, add_time, goods_id) values 
(4,'banner/banner1.jpg',0,'1970-01-01 20:08:53' at line 1")

经过测试是因为插入字段中含有关键字index
"""