# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:16:16 2018

@author: Administrator
"""
import csv  
import numpy as np
data=open('data.csv','r',encoding='utf-8')
read=csv.reader(data)
darr=[]
for row in read:
    darr.append(row)
nparr=np.array(darr)
x=nparr[:,:-1]
y=nparr[:,-1]    