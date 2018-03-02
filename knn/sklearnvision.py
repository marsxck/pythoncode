# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 09:52:47 2018

@author: Administrator
"""
from sklearn import neighbors
from sklearn import datasets
import numpy as np
knn=neighbors.KNeighborsClassifier()
iris=datasets.load_iris()

knn.fit(iris.data,iris.target)
print(iris.data,iris.target)
p=[1,2,3,4]
m=np.array(p)
res=knn.predict(m.reshape(1,-1))
print(res)