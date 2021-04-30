# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:02:04 2020

@author: ACER PREDATOR
"""

l1=[]
data1=int(input("小明身上有幾元："))
data2=int(input("販賣機有幾種飲料："))
data4 =0
for i in range(1,data2+1):
    data3=int(input("請輸入第%d種飲料價格：" %(i)))
    l1.append(data3)
    if l1[i-1] <= data1:
        data4 += 1
print("可以購買%d種飲料" %(data4))

        
        