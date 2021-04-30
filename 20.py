# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n=int(input("請輸入n："))
k=int(input("請輸入k："))
if k>1:
    ans=n//k
if ans>1:
    ans1=ans//k
ans2=ans1+ans+n
print("Peter可以抽%d支紙菸" % (ans2))