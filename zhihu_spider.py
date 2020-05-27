#!/user/bin/python
# _*_ coding:utf-8 _*_
import re
import time
from tkinter.filedialog import askdirectory
import tkinter as tk
import requests
import pandas as pd

__author__ = "super.gyk"


class ZhiHuSpider:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36"
        }
        self.pandas_data = []

    def get_answer(self, qid, offset):
        """
        利用知乎api请求json数据
        :param qid: 知乎问题号
        :param offset: 第几页
        :return:
        """
        url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=content&limit=20&offset={}" \
              "&platform=desktop&sort_by=default".format(qid, offset)
        response = requests.get(url, headers=self.headers)
        # print(response.status_code, type(response.status_code))
        if response.status_code == 200:
            response.encoding = "utf-8"
            # print(response.content)
            return response.json()

    def get_data(self, qid, file_name, file_path):
        # 去除文件路径中的换行符
        file_path = file_path.replace('\n', '')
        # print(file_path, "XXXXXXXXXX")
        offset = 0
        # num = 0
        # data2 = set()
        movie_data = {}
        while True:
            qid = qid
            print('Offset =', offset)
            # 知乎api请求
            data = self.get_answer(qid, offset)
            # print(data)
            if len(data['data']) == 0:
                break
            for line in data['data']:
                # 保存回答数据
                content = line['content']
                result = re.findall(r'《(.*?)》', content)
                # if ips.empty():
                #     get_ip()
                for name in result:
                    if "<a" in name:
                        name = name.split('>')[1].split("<")[0]
                    # print(name)
                    if "<b" in name:
                        name = name.strip().replace("<b>", '').replace('</b>', '')
                    if "<i" in name:
                        name = name.strip().replace('<i>', '').replace('</i>', '')
                    movie_data[name] = movie_data.get(name, 0) + 1
            offset += 20
            time.sleep(1)
        for i in movie_data.keys():
            new_data = {}
            if i:
                new_data['书籍名称'] = i
                new_data['频率'] = movie_data[i]
                self.pandas_data.append(new_data)
        df2 = pd.DataFrame(self.pandas_data, columns=['书籍名称', '频率'])
        # df2.to_csv("books.csv", encoding="utf_8_sig")
        df2.to_csv(file_path + "/" + file_name, encoding="utf_8_sig")

    def show_original_pic(self, text):
        """
        放入文件
        :param text:
        :return:
        """
        path = askdirectory(title="选择文件路径")
        text.delete(1.0, tk.END)
        text.tag_config("red", foreground="RED")
        text.insert(tk.END, path, "red")

    def main(self):
        # 实例化object，建立窗口
        window = tk.Tk()
        # 给窗口的可视化取名
        window.title("知乎书单提取：aKai")
        # 设置窗口大小(长*宽)
        window.geometry("500x500")

        # 问题号：id
        la1 = tk.Label(window, text="知乎问题号：")
        la1.place(x=50, y=50, width=100)

        v1 = tk.IntVar()
        question = tk.Entry(window, textvariable=v1)
        question.place(x=150, y=50)

        # 打开本地文件
        b1 = tk.Button(window, text='保存文件路径', command=lambda: self.show_original_pic(file_path))
        b1.place(x=60, y=100)
        # 文件路径地址 获取Text文本用get()
        # 注：get("0.0", tk.END)中"0.0"代表从第零行第零列开始，END到最后一个字符
        file_path = tk.Text(window, width=20, height=2)
        file_path.place(x=150, y=100)

        # 保存文件名
        la2 = tk.Label(window, text="保存文件名：")
        la2.place(x=50, y=150, width=100)
        # 文件名输入框，获取Entry文本用get()
        v2 = tk.StringVar()
        file_name = tk.Entry(window, textvariable=v2)
        file_name.place(x=150, y=150)

        # 开始爬取按钮
        b2 = tk.Button(window, text='数据提取', bg="green", fg="white", width=7, compound='center',
                       command=lambda: self.get_data(question.get(), file_name.get(), file_path.get("0.0", tk.END)))
        b2.place(x=50, y=250)

        tk.mainloop()


if __name__ == "__main__":
    spider = ZhiHuSpider()
    spider.main()
    # 281789365

# guanguanjujiu218