# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 08:25:20 2018

@author: Administrator
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#生成样本
x_data=np.linspace(1,-1,200)[:,np.newaxis]
nosie=(np.random.random(x_data.shape)-0.5)*0.3
y_data=np.square(x_data)+nosie


#构建神经网络10个神经元
#构建输入层
x=tf.placeholder(tf.float32,[None,1])
y=tf.placeholder(tf.float32,[None,1])
#构建中间层
weight_l1=tf.Variable(tf.random_normal([1,10]))
bis_l1=tf.Variable(tf.zeros([1,10]))
wx_plus_b_l1=tf.matmul(x,weight_l1)+bis_l1
L1=tf.nn.tanh(wx_plus_b_l1)
##构建输出层
Weights_L2=tf.Variable(tf.random_normal([10,1]))
biases_L2=tf.Variable(tf.zeros([1,1]))
#Wx_plus_b_L2=tf.matmul(L1,Weights_L2)+bis_l2
#prediction=tf.nn.tanh(Wx_plus_b_L2)
#定义神经网络中间层
#Weights_L1 = tf.Variable(tf.random_normal([1,10]))
#biases_L1 = tf.Variable(tf.zeros([1,10]))
#Wx_plus_b_L1 = tf.matmul(x,Weights_L1) + biases_L1
#L1 = tf.nn.tanh(Wx_plus_b_L1)

#定义神经网络输出层
#Weights_L2 = tf.Variable(tf.random_normal([10,1]))
#biases_L2 = tf.Variable(tf.zeros([1,1]))
Wx_plus_b_L2 = tf.matmul(L1,Weights_L2) + biases_L2
prediction = tf.nn.tanh(Wx_plus_b_L2)

#损失函数
loss=tf.reduce_mean(tf.square(prediction-y))

#优化器
opt=tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#创建会话
with tf.Session() as se:
    se.run(tf.global_variables_initializer())
    for _ in range(2000):
        se.run(opt,feed_dict={x:x_data,y:y_data})
    predict=se.run(prediction,feed_dict={x:x_data})
    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,predict)
    plt.show()






















 
