# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:47:46 2020

@author: ACER PREDATOR
"""
print("遊戲規則：你可以出 1.2.3.4.5 這五個數字 1 比 5 大、2比1大、3比2大、4比3大、5比4大。輸入一連串數字為甲方的數字，輸入一連串數字為乙的數字，兩者相比，判斷贏或輸或和局。")
a=list(input("甲方的數字："))
b=list(input("乙方的數字："))
e=""
for i in range(0,len(a)):
    if a[i]>b[i]:
        c="和"
        e=e+c
    else:
        d="輸"
        e=e+d
print("洗刷刷結果："+e)