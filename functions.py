#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:18:54 2020

@author: furkanaydin
"""


#FUNCTIONS

print()

?print

?len


print('a','b',sep='_',end=';')

3**2

lst = [1,2,3]
def make_square(val):
    print(val**2)

make_square(4)

def calculate_perdorm(isi,nem,sarj):
    return (isi + nem)/sarj
    

calculate_perdorm(10,20,15)


threshold = 5000
money = 5000

if money < threshold:
    print("gelir sinirdan kucuk")
elif money > threshold:
    print("gelir sinirdan buyuk")
else:
    print("Eşit")