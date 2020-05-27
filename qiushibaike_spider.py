#!/user/bin/python
# _*_ coding:utf-8 _*_
import requests
from lxml import etree

__author__ = "super.gyk"


class QiuSpider:
    def __init__(self):
        self.start_url = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
        }

    def get_url_list(self):
        url_list = [self.start_url.format(i) for i in range(1, 4)]
        return url_list

    def get_content(self, url):
        print("now parsing:", url)
        response = requests.get(url, headers=self.headers)
        xml = response.content.decode()
        html = etree.HTML(xml)

        content_list = html.xpath('//a[@class="text"]//text()')
        with open('qiuspider.txt', 'a', encoding='utf-8') as f:
            for content in content_list:
                f.write(content + "\n")
        print("保存成功！")

    # pyinstaller 可将python文件打包成.exe文件
    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            self.get_content(url)


if __name__ == "__main__":
    start = QiuSpider()
    start.run()
