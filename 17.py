# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:30:13 2020

@author: ACER PREDATOR
"""

data1=int(input("輸入金額："))
a=0
b=0
c1 = data1 % 100
c2 = c1 % 50
c3 = c2 % 10
c4 = c3 % 5
if data1 // 100 != 0:
    a = data1 // 100
    b += a        
if c1 // 50 != 0:
    a = c1 // 50
    b += a
if c2 // 10 != 0:
    a = c2 // 10
    b += a   
if c3 // 5 != 0:
    a = c3 // 5
    b += a
if c4 // 1 !=0:
    a = c4 // 1
    b += a 
print(b)
    