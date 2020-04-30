#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:35:55 2020

@author: furkanaydin
"""


#DATA STRUCTURES - Dictionary

dic = {'reg':'regresyon modeli',
       'loj':'lojistik regresyon',
       'cart':'classification and Reg'}

dic
len(dic)

dic['loj']

dic = {'reg':{'rms':10,
              'abd':20,
              'def':30},
       
       'loj':{'rms':10,
              'abd':20,
              'def':30},
       
       'cart':{'rms':10,
              'abd':20,
              'def':30}}

dic
dic['reg']['abd']
