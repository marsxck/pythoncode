# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:25:09 2018

@author: Administrator
"""
import tensorflow as tf
v1=tf.Variable(0)
init=tf.global_variables_initializer()
new_value=tf.add(v1,1)
update=tf.assign(v1,new_value)
with tf.Session() as se:
    se.run(init)
    for _ in range(0,5):
        res=se.run(update)
        print(se.run(v1))
