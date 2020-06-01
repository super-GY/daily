#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"

"""
读取Excel文件并写入到mysql数据库中
"""

import pymysql
import xlrd
import sys

'''
  连接数据库
  args：db_name（数据库名称）
  returns:db

'''


def mysql_link(de_name):
    try:
        db = pymysql.connect(host="127.0.0.1", user="root",
                             passwd="123456",
                             db="lang",
                             charset='utf8')
        return db
    except:
        print("could not connect to mysql server")


'''
  读取excel函数
  args：excel_file（excel文件，目录在py文件同目录）
  returns：book
'''


def open_excel(excel_file):
    try:
        book = xlrd.open_workbook(excel_file)  # 文件名，把文件与py文件放在同一目录下
        # print(sys.getsizeof(book))
        return book
    except:
        print("open excel file failed!")


'''
  执行插入操作
  args:db_name（数据库名称）
     table_name(表名称）
     excel_file（excel文件名，把文件与py文件放在同一目录下）

'''


def store_to(db_name, table_name, excel_file):
    # 连接数据库
    db = mysql_link(db_name)
    # 创建游标对象
    cursor = db.cursor()
    # 打开excel文件
    data = open_excel(excel_file)
    # 获取所有sheet表名
    sheets = data.sheet_names()
    for sheet in sheets:
        # 打开每一张表
        sh = data.sheet_by_name(sheet)
        # 表行数
        row_num = sh.nrows
        print(row_num)
        list = []  # 定义列表用来存放数据
        # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        for i in range(1, row_num):
            # 按行获取excel的值
            row_data = sh.row_values(i)
            value = (row_data[0], row_data[1], row_data[2], row_data[3])
            # 将数据暂存在列表
            list.append(value)
            sql = "INSERT INTO " + table_name + "(id, image, link_url, is_active) values (%s,%s,%s,%s)"
            # 执行sql语句
            cursor.execute(sql, value)
            print("worksheets: " + sheet + " has been inserted!")

    print("all worksheets has been inserted ")
    db.commit()  # 提交
    cursor.close()  # 关闭连接
    db.close()


if __name__ == '__main__':
    store_to('lang', 'lang_banner', 'banner2020-05-29.xls')
