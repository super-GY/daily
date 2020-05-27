#!/user/bin/python
# _*_ coding:utf-8 _*_
# 多线程爬取幽默笑话 2020/5/21
__author__ = "super.gyk"

import requests
import threadpool
import time
import os, sys
import re
from lxml import etree
from lxml.html import tostring


class ScrapDemo:
    """
    每页需要进入“查看更多”链接下面网页进行进一步爬取内容每页查看更多链接内容比较多，多任务进行，这里采用线程池的方式，
    可以有效地控制系统中并发线程的数量。避免当系统中包含有大量的并发线程时，导致系统性能下降，
    甚至导致 Python 解释器崩溃，引入线程池，花费时间更少，更效率。

    创建线程池threadpool.ThreadPool()
    创建需要线程池处理的任务即threadpool.makeRequests()，makeRequests存放的是要开启多线程的函数，
    以及函数相关参数和回调函数，其中回调函数可以不写（默认是无）
    将创建的多个任务put到线程池中,threadpool.putRequest()
    等到所有任务处理完毕theadpool.pool()

    """

    def __init__(self):
        self.next_page_url = ""  # 下一页的url
        self.page_num = 1
        self.detail_url_list = 0  # 详情页面的url地址
        self.depth = 0  # 抓取深度
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
        }
        self.file_num = 0

    def thread_index(self, url_list):  # 开启线程池
        if len(url_list) == 0:
            print("请输入需要爬取的地址")
            return False
        self.detail_url_list = len(url_list)
        pool = threadpool.ThreadPool(len(url_list))  # 创建线程池(num_workers, 线程数量)
        request_items = threadpool.makeRequests(self.detail_scray, url_list)  # 创建线程池处理的任务

        for item in request_items:
            pool.putRequest(item)   # put到线程池中
            time.sleep(0.5)
            pool.wait()

    def detail_scray(self, relative_url):  # 获取html 结构
        if not relative_url == "":
            url = "http://xiaohua.zol.com.cn/{}".format(relative_url)
            request = requests.get(url, headers=self.headers)
            html = request.text
            self.download_content(html)

    def download_content(self, ele):  # 抓取数据并存为TXT文件
        content_list = re.findall('<div class="article-text">(.*?)</div>', ele, re.S)
        for index in range(len(content_list)):
            # 使用正则表达式过滤掉回车、制表符和p标签
            content_list[index] = re.sub(r'(\r|\t|<p>|</p>)+', '', content_list[index])
        content = "".join(content_list)
        basedir = os.path.dirname(__file__)
        file_path = os.path.join(basedir)
        filename = "xiaohua{0}-{1}.txt".format(self.depth, str(self.file_num))
        file = os.path.join(file_path, 'xiaohua', filename)
        try:
            f = open(file, 'a', encoding='utf-8')
            f.write(content)
            if self.file_num == (self.detail_url_list - 1):
                print("下一页：", self.next_page_url)
                print("深度：", self.depth)
                if not self.next_page_url == "":
                    self.scrapy_start(self.next_page_url)
        except Exception as e:
            print("Error:%s" % str(e))
        self.file_num = self.file_num + 1
        print("此页文件数量：", self.file_num)

    def scrapy_start(self, url):
        if not url == "":
            self.file_num = 1
            self.depth = self.depth + 1
            print("开启第{0}页抓取".format(self.page_num))
            request = requests.get(url, headers=self.headers)
            html = request.text
            element = etree.HTML(html)
            all_url_list = element.xpath("//a[@class='all-read']/@href")  # 当前页面所有查看全文
            next_page_relative_url = element.xpath("//a[@class='page-next']/@href")  # 获取下一页的url(相对地址)
            self.next_page_url = 'http://xiaohua.zol.com.cn/{}'.format(next_page_relative_url[0])
            if not len(next_page_relative_url) == 0 and self.next_page_url != url:
                self.page_num = self.page_num + 1
                self.thread_index(all_url_list[:])
            else:
                print("下载完成，当前页数为{}页".format(self.page_num))
                sys.exit()
        else:
            print("起始路由有问题！")


if __name__ == "__main__":
    # http://xiaohua.zol.com.cn/youmo/
    start_url = "http://xiaohua.zol.com.cn/youmo/"
    # url = ""
    spider = ScrapDemo()
    spider.scrapy_start(url=start_url)
