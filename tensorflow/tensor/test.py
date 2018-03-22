# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 08:59:14 2018

@author: Administrator
"""

import tensorflow as tf
m1=tf.constant([[2,2]])
m2=tf.constant([[2],[2]])
oper=tf.matmul(m1,m2)
with tf.Session() as se:
    res=se.run(oper)
    print(res)