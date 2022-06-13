# -*- codeing = utf-8 -*-
# @time : 2022/4/19 0019 9:36
# @Author :马国鼎
# @File : demo2.py
# @Software:PyCharm
try:
    a = int(input('请输入一个整数:'))
    b = int(input('请输入一个整数:'))
    result =a/b
except ZeroDivisionError:
    print('除数不能为0')
else:
    print(result)
    print('程序结束')
