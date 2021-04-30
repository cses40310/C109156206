# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 09:02:49 2020

@author: 陳博劭
"""

a=""
data1=input("輸入值為:").split(",")
data1.sort()
m = sorted(data1, reverse = True)
m2=int(a.join(data1))
m1=int(a.join(m))
print("最大值數列與最小值數列差值為:"+str(m1-m2))
