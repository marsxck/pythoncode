# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:38:18 2018

@author: Administrator
"""

import numpy as np
def tan_deriv(x):
    return 1-np.tanh(x)*np.tanh(x)
def tanh(x):
    return np.tanh(x)
def logistic(x):
    return 1/(1+np.exp(-x))
def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))
weights = []
weights.append((2*np.random.random((2, 3))))
a=weights[:,0:-1]
          