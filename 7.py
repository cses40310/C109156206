# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 06:59:24 2020

@author: ACER PREDATOR
"""

data1=int(input("請輸入第一行正整數："))
data2=input("第二行中數列中的數字為：").split(" ")
list1=[]
for i in range(1,data1+1):
    list1.append(data2.count(str(i)))
m=max(list1)
if m==1:
    print("每個數字剛好只出現1次")
else:
    print("最大出現次數的數字為:",list1.index(m)+1)
    print("出現次數為:",m)