#!/user/bin/python
# _*_ coding:utf-8 _*_
from random import choice

__author__ = "super.gyk"


def generate_code(seeds):
    """
    生成验证code
    :return:
    """
    # seeds = "23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
    random_str = []
    for i in range(4):
        random_str.append(choice(seeds))

    # return "".join(random_str)
    str_1 = "".join(random_str)
    print(str_1)


generate_code("23456789ABCDEFGHJKLMNPQRSTUVWXYZ")
