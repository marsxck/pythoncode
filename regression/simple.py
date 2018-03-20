# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 10:28:37 2018

@author: Administrator
"""
import numpy as np
def fit(x,y):
    nLen=len(x)
    numerator=0.0
    dinominator=0.0
    for i in range(nLen):
        numerator+=(x[i]-np.mean(x))*(y[i]-np.mean(y))
        dinominator+=(x[i]-np.mean(x))**2
    b1=numerator/dinominator
    b0=np.mean(y)-b1*np.mean(x)
    return b1,b0
def predit(x,b0,b1):
    return x*b1+b0
x=[1,3,2,1,3]
y=[14,24,18,17,27]
c=np.mean(x)
a,b=fit(x,y)
res=predit(5,a,b)

