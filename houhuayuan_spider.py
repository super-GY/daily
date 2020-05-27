#!/user/bin/python
# _*_ coding:utf-8 _*_
# 2020/5/21
__author__ = "super.gyk"

import re

import requests
from lxml import etree

# 爬虫实战：爬取笑话段子

# 第1页的URL：http://www.lovehhy.net/Joke/Detail/QSBK/1
# 第2页的URL：http://www.lovehhy.net/Joke/Detail/QSBK/2
# 第3页的URL：http://www.lovehhy.net/Joke/Detail/QSBK/3
# 故可以得到请求的URL公式：url="http://www.lovehhy.net/Joke/Detail/QSBK/"+page_index
# 其中page_index为页码

# 打印的页数
page_num = int(input("请输入您要获取多少页笑话："))
for index in range(1, page_num + 1):
    # 请求的URL
    # url = "http://www.lovehhy.net/Joke/Detail/QSBK/" + str(index)
    url = "http://www.lovehhy.net/Joke/Detail/NHLXH/" + str(index)

    # 发送请求，获取响应到的HTML源码
    response = requests.get(url).text
    # 处理换行问题，如果不处理，只会得到一行的内容
    response = re.sub("<br />", "", response)
    # 将HTML源码字符串转换成HTML对象
    html = etree.HTML(response)
    # 获取所有笑话的标题
    data_title_list = html.xpath("//div//h3/a/text()")
    # print(data_title_list)
    # 获取所有笑话的内容
    data_content_list = html.xpath("//div//div[@id='endtext']/text()")
    # 打印到控制台
    f = open('houhuayuan.txt', 'a', encoding='utf-8')

    if len(data_title_list) == len(data_content_list):
        for i in range(0, len(data_title_list)):
            content = data_title_list[i] + "\n" + data_content_list[i] + "\n\n"
            f.write(content)

# http://www.lovehhy.net/Joke/
# http://www.lovehhy.net/Default.aspx?LX=NHDZ
# http://www.lovehhy.net/Default.aspx?LX=NHDZ&PG=2
