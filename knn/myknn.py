# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:21:53 2018

@author: Administrator
""" 

import math
import numpy as np
import csv
import random
import operator
def loaddata(filename,learnset,testset):
    read=open(filename,'r')
    data=csv.reader(read)
    dataset=list(data)
    for x in range(len(dataset)):
        for y in range(4):
            dataset[x][y] = float(dataset[x][y])
        if random.random()<0.66:
            learnset.append(dataset[x])
        else:     
            testset.append(dataset[x])
def getinst(instance,learnset,insset):
    for i in range(len(learnset)-1):
        ins=0
        for j in range(4):
            ins+=math.pow(instance[j]-learnset[i][j],2)
        #if(math.sqrt(ins)==0.0):
            #insset.append([10000000,learnset[i]])
        #else:
        insset.append([math.sqrt(ins),learnset[i]])

def getres(instance,learnset,k=3):
    insset=[]
    getinst(instance,learnset,insset)
    insset.sort()
    dic={}
    for i in range(k):
        res=insset[i][1][-1]
        if res in dic:
            dic[res]+=1
        else:
            dic[res]=1
    sorteddic=sorted(dic.items(),key=lambda d:d[1],reverse=True)
    return sorteddic[0][0]
def getrat(testset,res):
    correct=0
    for i in range(len(testset)):
        if res[i]==testset[i][-1]:
            correct+=1;
    return correct/len(testset)*100
def main():
    learnset=[]
    testset=[]
    res=[]
    loaddata('irisdata.txt',learnset,testset)
    print("learnset len:%d\ttestset len:%d"%(len(learnset),len(testset)))
    for i in range(len(testset)):
        a=getres(testset[i],learnset,k=5)
        res.append(a)
    temp=getrat(testset,res)
    print(temp)
if __name__=='__main__':
    main()