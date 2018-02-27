# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:34:21 2018

@author: Administrator
"""

import os
import time
res='D:\老毛桃'
tra='D:\hh'+time.strftime('%Y%m')+'.zip'
com="rar a %s %s"%(tra,res)
a=os.system(com)

