# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:36:25 2020

@author: ACER PREDATOR
"""

l1=[]
l2=["國文","英文","微積分","體育","程式設計"]
a=int(input("國文："))
l1.append(a)
b=int(input("英文："))
l1.append(b)
c=int(input("微積分："))
l1.append(c)
d=int(input("體育："))
l1.append(d)
e=int(input("程式設計："))
l1.append(e)
avg=sum(l1)/len(l1)
m1=max(l1)
m2=min(l1)
print("平均分數：%d分" %(avg))
print("最高分科目：%s：%d分" %(l2[l1.index(m1)],m1))
print("最低分科目：%s：%d分" %(l2[l1.index(m2)],m2))