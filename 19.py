# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:19:40 2020

@author: ACER PREDATOR
"""
letter_morse={"0":"-----","1":".----","2":"..---","3":"...--",
              "4":"....-","5":".....","6":"-....","7":"--...",
              "8":"---..","9":"----."}
b=""
c=input("請輸入數字：").lower()
print(c)
for letter in c:
    if letter not in letter_morse:
        print("coudn't find " + letter +".")
    
    elif letter in c:
        b += letter_morse[letter] + ""
print(b)
    
