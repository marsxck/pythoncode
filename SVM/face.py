# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 21:59:07 2018

@author: Administrator
"""
import logging
from time import time
from sklearn.datasets import fetch_lfw_people
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import RandomizedPCA
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=.01, right=.99, top=.90, hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())
logging.basicConfig(level=logging.info,format='%(asctime)s %(message)s')
#加载图片
t0=time()
lfw_people = fetch_lfw_people(data_home='E:\study\Python\pythoncode\SVM',min_faces_per_person=50, resize=0.4,download_if_missing=False)
print(u'加载数据花费%0.3fs'%(time()-t0))
#数据集信息
nNum,h,w=lfw_people.images.shape
X=lfw_people.data
nFeature=X.shape[1]
Y=lfw_people.target
strName=lfw_people.target_names
print(u'样本数为%d'%nNum)
print(u'特征数为%d'%nFeature)
print(u'类别%d'%len(strName))
#划分训练集和测试集
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.25)
#PCA特征提取模型建立
nCom=200
print(u'从训练集%d个样本中，每个提取%d个特征值组成特征脸'%(X_train.shape[0],nCom))
t0=time()
pca=RandomizedPCA(n_components=nCom,whiten=True).fit(X_train)
print(u'建立pca特征脸模型花费时间%0.3fs'%(time()-t0))
ftface=pca.components_.reshape((nCom,h,w)) 
ftface_title=['ftface %d'%i for i in range(ftface.shape[0])]
plot_gallery(ftface,ftface_title,h,w)
#数据降维
t0=time()
X_train_pca=pca.transform(X_train)
X_test_pca=pca.transform(X_test)
print('降维花费时间%0.3fs'%(time()-t0))
#训练SVM分类器
print(u'开始训练svm')
t0=time()
param={'C':[1e3,5e3,1e4,5e4,1e5],'gmma':[0.0001,0.0005,0.001,0.005,0.01,0.1]}
clf=svm.SVC(kernel='rbf')
clf=clf.fit(X_train_pca,Y_train)
print(u'花费时间%0.3fs'%(time()-t0))
#使用测试集评估模型
print("预测测试集")
t0 = time()
Y_pred = clf.predict(X_test_pca)
print("花费时间%0.3fs" % (time() - t0))
print(classification_report(Y_test, Y_pred, target_names=strName))
print(confusion_matrix(Y_test, Y_pred, labels=range(len(strName))))
# 图形化结果
def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[y_test[i]].rsplit(' ', 1)[-1]
    return 'predicted: %s\ntrue:      %s' % (pred_name, true_name)

prediction_titles = [title(Y_pred, Y_test, strName, i)\
                     for i in range(Y_pred.shape[0])]

plot_gallery(X_test, prediction_titles, h, w)
plt.show()


