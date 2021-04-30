# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 05:08:28 2020

@author: ACER PREDATOR
"""

a=b=1
m=int(input("請輸入正整數m的值："))
while(a<=m):
    b+=1
    a*=b
print("超過M為%d的最小階層N值為：%d" % (m,b))