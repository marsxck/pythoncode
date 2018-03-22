# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:06:15 2018

@author: Administrator
"""
import tensorflow as tf
c1=tf.constant(3.0)
c2=tf.constant(4.0)
c3=tf.constant(5.0)
add=tf.add(c1,c2)
mut=tf.multiply(add,c3)
with tf.Session() as se:
    res=se.run([add,mut])#fetch
c4=tf.placeholder(tf.float32)
c5=tf.placeholder(tf.float32)
mut=tf.multiply(c4,c5)
with tf.Session() as se:
    res=se.run(mut,feed_dict={c4:[4.],c5:[7.]})
    print(res)
