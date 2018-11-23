# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:03:23 2018
@author: wmy
"""

import numpy

def FileMatrixTransfer(filename):
    fr=open(filename)
    arrayolines=fr.readlines()
    numberoflines=len(arrayolines)
    #每行元素个数
    returnmat=numpy.zeros((numberoflines,3))
    classlabelvector=[]
    index=0
    for line in arrayolines:
        line=line.strip()
        listfromline=line.split('\t')
        #从第几个到第几个元素
        returnmat[index,:]=listfromline[0:3]
        #传回一列
        classlabelvector.append(int(listfromline[-1]))
        index+=1
    return returnmat,classlabelvector

mat,labels=FileMatrixTransfer('filetest.txt')
print(mat)
print(labels)
