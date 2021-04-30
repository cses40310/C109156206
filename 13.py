# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 04:09:16 2020

@author: ACER PREDATOR
"""

m=int(input("請輸入月份："))
d=int(input("請輸入日："))
s=(m*2+d)%3
if s == 0:
    print("普通")
elif s == 1:
    print("吉")
elif s == 2:
    print("大吉")