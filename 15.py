# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 02:25:50 2020

@author: ACER PREDATOR
"""

dict1 = {"1A":"127","1B":"140","2A":"117","2B":"130",
         "3A":"137","3B":"150","4A":"99","4B":"112","5A":"115","5B":"128"}
data1 = input("請選擇主餐及升級的套餐：")
if data1 in dict1:
    a = int(dict1[data1])
data2 = input("是否升級成大杯飲料：")
if data2 == "是":
    b = a + 7
else:
    b = a
data3 = input("是否換成大薯：")
if data3 == "是":
    c = b + 13
else:
    c = b
print("總共為%4d 元" % (c))
    