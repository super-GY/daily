#!/user/bin/python
# _*_ coding:utf-8 _*_
__author__ = "super.gyk"

# encoding=utf8
import random
import string


class RedeemCodeGeneration():

    def __init__(self):
        self.str_code = string.ascii_letters + string.digits

    def redeem_generation(self, lens):
        code = ''
        for i in range(1, lens + 1):
            code += random.choice(self.str_code)
            if i % 4 == 0 and i != lens:
                code += '-'
        return code

    def get_all_redeem(self, lens, num):
        code_list = []
        for i in range(num):
            redeem_code = self.redeem_generation(lens)
            if redeem_code not in code_list:
                code_list.append(redeem_code)
        print(code_list, len(code_list))


if __name__ == "__main__":
    start = RedeemCodeGeneration()
    le = int(input("请输入要生成的随机码长度:"))
    n = int(input("请输入要生成的随机码个数:"))
    start.get_all_redeem(le, n)
