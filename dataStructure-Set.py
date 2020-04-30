#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:27:20 2020

@author: furkanaydin
"""


# DATA STRUCTURE - Set

s = set()

lst = [1,2,3,40]
s = set(lst)
s

set1 = set([1,2,3,4])
set2 = set([1,2,3,5])

set1.difference(set2) #set1 de olup set2 de olmayanlar
set2.difference(set1) #set2 de olup set1 de olmayanlar

set1.symmetric_difference(set2) # her ikisinde de olmayanalar

set1 - set2
set2 - set1

set1.intersection(set2)
set1 & set2

set1.union(set2)

set1.intersection_update(set2)
set1


#Set Sorgu İşlemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])


set1.isdisjoint(set2)

set1.issubset(set2)

set2.issuperset(set1)
