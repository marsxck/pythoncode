# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:38:18 2018

@author: Administrator
"""

import numpy as np
def tan_deriv(x):
    return 1.0-np.tanh(x)*np.tanh(x)
def tanh(x):
    return np.tanh(x)
def logistic(x):
    return 1/(1+np.exp(-x))
def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))
class NeuralNetwork:
    def __init__(self,Layers,activation):
        """初始化（layers=[2,3,1],activation='tanh'）
        """
        if activation=='tanh':
            self.activation=tanh
            self.deriv=tan_deriv
        elif activation=='logistic':
            self.activation=logistic
            self.deriv=logistic_derivative
        if len(Layers)>3:
            print('error')
            exit(1)
        self.weights=[]
        self.weights.append((np.random.random((Layers[0],Layers[1]))*2-1))
        self.weights.append((np.random.random((Layers[1],Layers[2]))*2-1))
    def fit(self,X,Y,learnrato=0.2,epoch=10000):
        np.atleast_2d(X)
#        temp=np.ones([X.shape[0],X.shape[1]+1])
#        temp[:,0:-1]=X
#        X=temp
        Y=np.array(Y)#引入偏移 相当于输入加一个维度
        #向前传导
        for i in range(epoch):
            i=np.random.randint(X.shape[0])
            uintres=[X[i]]
            for j in range(len(self.weights)):
                uintres.append(self.activation(np.dot(uintres[j],self.weights[j])))
            error=Y[i]-uintres[-1]
            loss=[error*self.deriv(uintres[-1])]
            #BP
            for l in range(len(uintres)-2,0,-1):
                loss.append(loss[-1].dot(self.weights[l].T)*self.deriv(uintres[l]))
            loss.reverse()
            for i in range(len(self.weights)):
                layer=np.atleast_2d(uintres[i])
                los=np.atleast_2d(loss[i])
                self.weights[i]+=learnrato*layer.T.dot(los)
    def predict(self,X):
        X=np.array(X)
#        temp=np.ones(X.shape[0]+1)
#        temp[0:-1]=X
        a=X
        print(a.shape)
        for i in range(len(self.weights)):
#            print(a.shape[0])
            print(self.weights[i].shape)
            a=self.activation(np.dot(a,self.weights[i]))
        return a
nn = NeuralNetwork([2, 4,1], 'tanh')
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])
nn.fit(X, y)
for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    print(i, nn.predict(i))
          