# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 06:46:51 2020

@author: ACER PREDATOR
"""

data1,data2=eval(input("請輸入月租費型式及通話時間："))
if data1==186:
    if data2*0.09>186:
        data3=data2*0.09*0.8
    else:
        data3=data2*0.09*0.9
elif data1==386:
    if data2*0.08>386:
        data3=data2*0.08*0.7
    else:
        data3=data2*0.08*0.8
elif data1==586:
    if data2*0.07>586:
        data3=data2*0.07*0.6
    else:
        data3=data2*0.07*0.7
elif data1==986:
    if data2*0.06>986:
        data3=data2*0.07*0.6
    else:
        data3=data2*0.07*0.7
print("通話費為：%0.0f" %(data3))