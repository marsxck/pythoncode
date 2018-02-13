# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:36:21 2018

@author: Administrator
"""
import numpy
import matplotlib.pyplot as plot#数据获取
x,y,d=[],[],[]
for info in open('prices.txt','r'):
    x_,y_=info.split(',')
    x.append(float(x_))
    y.append(float(y_))

_x=numpy.array(x)
y=numpy.array(y)
x=(_x-_x.mean())/_x.std()
#画图
plot.figure()
plot.scatter(x,y,c='r',s=9)

#拟合函数
def GetP(rank):
    return numpy.polyfit(x,y,rank)#返回p序列
x0=numpy.linspace(-2,4,100)
for i in [1,4,10]:
    y0=numpy.polyval(GetP(i),x0)
    d.append((0.5*(numpy.polyval(GetP(i),x)-y)**2).sum())
    plot.plot(x0,y0)
plot.xlim(-2,4)
plot.ylim(1e5,8e5)
plot.legend(('degree=1 {}'.format(d[0]),'degree=4 {}'.format(d[1]),'degree=10 {}'.format(d[2])),loc='upper right')
plot.show()
value=float(input('输入面积'))
print('预测房价为：%d'%numpy.polyval(GetP(1),(value-_x.mean())/_x.std()))

    
    
