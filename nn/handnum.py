# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 10:05:46 2018

@author: Administrator
"""
from sklearn.datasets import load_digits
import nn
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelBinarizer
from time import time
import numpy as np
from sklearn.metrics import classification_report
digits=load_digits()
x=digits.data
y=digits.target
x-=x.min()
x/=x.max()
#标准化到0-1之间
clf=nn.NeuralNetwork([64,1000,10],'logistic')
#标准化y
x_train,x_test,y_train,y_test=train_test_split(x,y)
label_train=LabelBinarizer().fit_transform(y_train)
label_test=LabelBinarizer().fit_transform(y_test)
print(u'模型训练中。。。')
t0=time()
clf.fit(x_train,label_train)
print(u"训练耗时%0.3f秒"%(time()-t0))
pre=[]
for i in range(x_test.shape[0]):
    res=clf.predict(x_test[i])
    pre.append(np.argmax(res))
print(classification_report(y_test,pre))


   