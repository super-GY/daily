#!/user/bin/python
# _*_ coding:utf-8 _*_
from weathers import city
from urllib import request
import re

__author__ = "super.gyk"


class WeatherQuery():

    def __init__(self):
        self.url = 'https://tianqi.so.com/weather/'
        # 包含天气日期星期的html代码段
        self.weather_week = '<ul class="weather-columns"><li>([\s\S]*?)</li'
        # 日期与星期
        self.week = '<!-- ([\S\s]*?) -->'
        # 日期与星期
        self.data = '-->([\s\S]*?)</div>'
        # 包含天气的代码段
        self.weather = r'<div class="weather-icon weather-icon-([\s\S]*?)\n'

        # 包含指数的html的代码段
        self.index_data = r'<div class="tab-pane"([\S\s]*?)</div></div></div>'
        # 指数
        self.index_index = '<div class="tip-title tip-icon-([\S\s]*?)">'
        # 建议
        self.index_sugge = '<div class="tip-cont" title="([\s\S]*?)"'
        # 城市名称
        self.city_n = ""

    # 模拟http请求获取html
    def get_html(self, codes):
        url = str(self.url + codes)
        response = request.urlopen(url)
        html = response.read()
        html = str(html, encoding='utf-8')

        return html

    def analyze(self, ff, html):
        # 天气
        if ff == 1:
            weather_weeks = re.findall(self.weather_week, html)
        # 指数
        else:
            weather_weeks = re.findall(self.index_data, html)

        return weather_weeks

    # 查询近期十五天之内的天气
    def analyze_weather(self, weather_weeks):

        star_lists = []

        for we in weather_weeks:
            data_l = re.findall(self.data, we)  # 分割星期，日期
            weather_l = re.findall(self.weather, we)  # 天气

            data_ll = data_l[0].split()
            week1 = data_ll[0]  # 星期
            data1 = data_ll[1]  # 日期
            weat = weather_l[0].split()
            weather_l = weat[1]  # 天气

            star_list = {'week': week1, "data": data1, "weather": weather_l}
            star_lists.append(star_list)

        return star_lists

    def analyze_indexes(self, index_code):

        star_indexes = []

        for ind in index_code:
            indexes = re.findall(self.index_index, ind)
            sugges = re.findall(self.index_sugge, ind)

            for i in (range(0, len(indexes) - 1)):
                res_index = indexes[i].split('"')
                star_index = {'index': res_index[2], 'sugges': sugges[i]}
                star_indexes.append(star_index)

        return star_indexes

    def show_weather(self, star_lists):
        print("***************** %s近十五天的天气如下：*************\n\n" % self.city_n)
        for re in star_lists:
            print("星期：" + re['week'] + "    日期：" + re['data'] + "   天气：" + re['weather'])
            # print(rs)

    def show_index(self, star_indexes):
        print("*****************  两天指数及建议： ****************\n")
        print("\n\n*****************  今天建议如下  *****************\n\n")
        l = 0
        for re in star_indexes:
            l = l + 1
            fg = re['index'].split("：")

            if fg[0] == "过敏指数":
                if l > 1:
                    print("\n\n*****************  明天建议如下  *****************\n\n")
            print(re['index'] + "\t         建议：" + re['sugges'])

    def city_num(self):

        city_name = input("请输入城市名：")
        code = city.citycode[city_name]
        self.city_n = city_name
        print("您查询的是" + city_name + "城市代码为：" + code)

        if not city_name in city.citycode:
            print("这个城市不存在！")
            exit()
            code = city.citycode[city_name]
        return code

    def run(self):
        codes = self.city_num()
        html = self.get_html(codes)

        # 查询天气
        weather_weeks = self.analyze(1, html)
        star_lists = self.analyze_weather(weather_weeks)
        # 查询指数
        indexes = self.analyze(2, html)
        star_indexes = self.analyze_indexes(indexes)

        # 展示天气
        self.show_weather(star_lists)
        # 展示指数
        self.show_index(star_indexes)


if __name__ == "__main__":
    wq = WeatherQuery()
    wq.run()

# 9200-5700=3500
