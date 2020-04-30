#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:33:42 2020

@author: furkanaydin
"""


#DATA STRUCTURES

#List

notes = [1,4,5,7,9]
type(notes)

lst = ['abc',12.4,45]
newList = ['ab',12.4,5,notes]
len(newList)

newList[0]
newList[3]

tum_liste = [lst,newList]
#del tum_liste

liste = [10,20,30,40,50]

liste[0:3]
liste[:3]
liste[1:]

liste = ['ali','veli','ayse']

liste[1] = 'kazim'
liste[:2] = 'mehemt','hasan'
liste

liste += ['kemal']
liste

# append() & remove()
liste.append('kamil')
liste
liste.remove('hasan')
liste

# insert() & pop()
liste.insert(0, 'sehra')
liste
liste.pop(1)
liste

#count()
liste = ['ali','veli','ayse','ali','veli']
liste.count('ayse')

#copy()
liste_yedek = liste.copy()

#extend
liste.extend(['a',12])
liste

#index()
liste.index('veli')

#reverse()
liste.reverse()
liste

#sort()
liste = [10,40,5,90]
liste.sort()
liste

#clear()
liste.clear()
liste




