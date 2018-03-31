# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:28:50 2018

@author: Administrator
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
#载入数据
data=input_data.read_data_sets('MNIST_data',one_hot=True)

#定义批次大小
batch_size=100
#批次个数
n_batch=data.train.num_examples//batch_size

#输入输出
x=tf.placeholder(tf.float32,[None,784])
y=tf.placeholder(tf.float32,[None,10])
drop=tf.placeholder(tf.float32)

#中间层
w1=tf.Variable(tf.truncated_normal([784,2000],stddev=0.1))
b1=tf.Variable(tf.zeros([2000])+0.1)
l1=tf.nn.tanh(tf.matmul(x,w1)+b1)
l1_drop=tf.nn.dropout(l1,drop)

#第二层
w2=tf.Variable(tf.truncated_normal([2000,2000],stddev=0.1))
b2=tf.Variable(tf.zeros([2000])+0.1)
l2=tf.nn.tanh(tf.matmul(l1,w2)+b2)
l2_drop=tf.nn.dropout(l2,drop)

#第三层
w3=tf.Variable(tf.truncated_normal([2000,1000],stddev=0.1))
b3=tf.Variable(tf.zeros([1000])+0.1)
l3=tf.nn.tanh(tf.matmul(l2,w3)+b3)
l3_drop=tf.nn.dropout(l3,drop)

#第四层
w4=tf.Variable(tf.truncated_normal([1000,10],stddev=0.1))
b4=tf.Variable(tf.zeros([10])+0.1)
l4=tf.nn.softmax(tf.matmul(l3,w4)+b4)
l4_drop=tf.nn.dropout(l4,drop)


#损失函数
#loss=tf.reduce_mean(tf.square(l2-y))
loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y,logits=l4_drop))

#优化器
opt=tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#准确度检验
correct=tf.equal(tf.argmax(y,1),tf.argmax(l4_drop,1))

#求准确率
accuracy=tf.reduce_mean(tf.cast(correct,tf.float32))


with tf.Session() as se:
    se.run(tf.global_variables_initializer())
    for epoch in range(209):
        for batch in range(n_batch):
            xs,ys=data.train.next_batch(batch_size)
            se.run(opt,feed_dict={x:xs,y:ys,drop:0.7})
        acc=se.run(accuracy,feed_dict={x:data.test.images,y:data.test.labels,drop:1})
        print(acc)
