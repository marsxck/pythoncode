# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:06:13 2018

@author: Administrator
"""
import tensorflow as tf
import numpy as np
x_data=np.random.rand(100)
y_data=x_data*5+4
#建立模型
k=tf.Variable(0.)
b=tf.Variable(0.)
y=k*x_data+b
#损失函数
loss=tf.reduce_mean(np.square(y-y_data))
#定义优化器
opt=tf.train.GradientDescentOptimizer(0.01)
#最小代价函数
train=opt.minimize(loss)
#初始化变量
init=tf.global_variables_initializer()
#创建会话
with tf.Session() as se:
    se.run(init)
    for step in range(10000):
        se.run(train)
        if step%100==0:
            print(step,se.run([k,b]))
    