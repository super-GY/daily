#!/user/bin/python
# _*_ coding:utf-8 _*_
# from gouPi.readJSON import read_json
import random
import json

__author__ = "super.gyk"


# 读取json文件
def read_json(file_name):
    if file_name != '':
        str_list = file_name.split(".")
        if str_list[len(str_list) - 1].lower() == "json":
            with open(file_name, mode='r', encoding="utf-8") as f:
                return json.loads(f.read())


# 获取json文件信息
data = read_json("data.json")
wisdom = data["famous"]  # 名人名言
before = data["before"]  # 前面垫话
after = data["after"]  # 后面垫话
bosh = data["bosh"]  # 废话

# 重复度
multiplicity = 1


# 获取随机句子
def get_element(sentence_list):
    global multiplicity
    pools = list(sentence_list) * multiplicity
    while True:
        random.shuffle(pools)
        for item in pools:
            yield item


# 下一句废话
after_bosh = get_element(bosh)
# 下一句名人名言
after_wisdom = get_element(wisdom)


# 获取名人名言并拼接成完整的一句话
def get_wisdom():
    global after_wisdom
    xx = next(after_wisdom)
    xx = xx.replace("a", random.choice(before))
    xx = xx.replace("b", random.choice(after))
    return xx


# 另起一段
def after_paragraph():
    xx = "。 "
    xx += "\r\n"
    xx += "    "
    return xx


if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while len(tmp) < 3000:
            branch = random.randint(0, 100)
            if branch < 5:
                tmp += after_paragraph()
            elif branch < 20:
                tmp += get_wisdom()
            else:
                tmp += next(after_bosh)
        tmp = tmp.replace("x", xx)
        print(tmp)
