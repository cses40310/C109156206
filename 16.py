# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:54:59 2020

@author: ACER PREDATOR
"""
import heapq
l1=[]
l2=[]
for i in range(1,11):
    data1 = int(input("請輸入第%d個數字：" % (i)))
    l1.append(data1)
for i in range(1,4):
    data2 = max(l1)
    l2.append(data2)
    l1.remove(data2)
l2.sort()
data = map(l1.index, heapq.nlargest(3, l1))
print("最大的 3 個數字為：%s" % (l2))