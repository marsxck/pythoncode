# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:35:02 2018

@author: Administrator
"""

from sklearn import svm
import numpy
X=[[2,3],[1,1],[2,0]]
Y=[0,1,1]
clf=svm.SVC(kernel='linear')
clf.fit(X,Y)
a=numpy.array([0,0])
res=clf.predict(a.reshape(1,-1))