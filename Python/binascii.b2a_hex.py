#!/usr/bin/python3
# -*- coding: utf-8 -*-


import binascii

a = 'Python'
print("a字符串值：",a)

# 字符串转为十六进制
b = binascii.b2a_hex(a.encode()) #注意：这里需要转换为编码格式，否则报错
print("b字符串值：",b)
