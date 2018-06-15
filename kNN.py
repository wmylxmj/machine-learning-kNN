# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy
import operator

def creatdataset():
    group = numpy.array([[1.0,1.1],[1.0,1.0],[0,0],[0.0,1]])
    labels = ['A','A','B','B']
    return group,labels


def classify0(inx,dataset,labels,k):
    datasetsize=dataset.shape[0]        
    diffmat=numpy.tile(inx,(datasetsize,1))-dataset  
    sqdiffmat=diffmat**2
    sqdistances=sqdiffmat.sum(axis=1)
    distances=sqdistances**0.5
    sorteddistindicies=distances.argsort()
    classcount={}        
    for i in range(k):
        voteilabel=labels[sorteddistindicies[i]]
        classcount[voteilabel]=classcount.get(voteilabel,0)+1
    sortedclasscount=sorted(classcount.items(),key=operator.itemgetter(1),reverse=True)    
    return sortedclasscount[0][0]


group,labels = creatdataset()
print(group)
print(labels)
    
print(classify0([0,0],group,labels,3))

