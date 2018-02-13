# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:36:21 2018

@author: Administrator
"""
import numpy
import matplotlib.pyplot as plot#数据获取
x,y=[],[]
for info in open('prices.txt','r'):
    x_,y_=info.split(',')
    x.append(float(x_))
    y.append(float(y_))

x=numpy.array(x)
y=numpy.array(y)
x=(x-x.mean())/x.std()
#画图
plot.figure()
plot.scatter(x,y,c='r',s=9)
plot.show()
