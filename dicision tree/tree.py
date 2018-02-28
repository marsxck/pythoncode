# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 20:57:02 2018

@author: Administrator
"""
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO
#导入文件
allElectronicsData=open('AllElectronics.csv', 'r')
reader = csv.reader(allElectronicsData)
feauterlist=[]
lablelist=[]
head=next(reader)
for row in reader:
    lablelist.append(row[len(row)-1])
    fu={}
    for i in range(1,len(row)-1):
        fu[head[i]]=row[i]
    feauterlist.append(fu)
print(lablelist)
#特征和label矢量化
vec=DictVectorizer()
X=vec.fit_transform(feauterlist).toarray()
lb=preprocessing.LabelBinarizer()
Y=lb.fit_transform(lablelist)
print(X,Y)
#生成决策树
clf=tree.DecisionTreeClassifier(criterion="entropy")
clf=clf.fit(X,Y)
#预测
p=X[0,:].reshape(1,-1)#将数组排列为1行n列
res=clf.predict(p)
print(res)

