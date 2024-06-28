#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
 
code='utf-8'
offset=b'python1234567890'  #字节
mykey='my_python_key_20230220ABC_ComeOn'    #支持16位和32位长度
key = mykey.encode(code)
mode = AES.MODE_CBC
 
# 加16位
def addTo16(txt):
    if len(txt.encode(code)) % 16:
        add = 16 - (len(txt.encode(code)) % 16)
    else:
        add = 0
    txt = txt + ('\0' * add)
    return txt.encode(code)
 
# 解密数据函数
def decryptData(text):
    cryptor = AES.new(key, mode,offset)
    plain_text = cryptor.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')
     
# 程序入口
if __name__ == '__main__':
    # 加密串
    text="06a9c834a3fa7a9774a0e0e319226f7f"
    # 解密串
    decryptStr = decryptData(text) 
                                    
    print("加密串数据:", text)
    print("解密串数据:", decryptStr)
