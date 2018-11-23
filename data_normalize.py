# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:02:03 2018
@author: wmy
"""

import numpy

def NormalizeData(dataset):
    minvalues=dataset.min(0)
    maxvalues=dataset.max(0)
    dataranges=maxvalues-minvalues
    normalizeddataset=numpy.zeros(numpy.shape(dataset))
    m=dataset.shape[0]
    normalizeddataset=dataset-numpy.tile(minvalues,(m,1))
    normalizeddataset=normalizeddataset/numpy.tile(dataranges,(m,1))
    return normalizeddataset,dataranges,minvalues,maxvalues
    
def CreatCommonColourTable():    
    ColourValue=numpy.array([[0,0,0],[192,192,192],[255,255,255],
                      [255,250,250],[255,0,0],[163,148,128],
                      [255,255,0],[65,105,225],[0,255,255],
                      [135,206,235],[127,255,0],[0,255,0],
                      [160,32,240],[221,160,221],[0,0,255],
                      [128,42,42],[107,142,35],[250,128,114]])
    ColourName=['黑色','灰色','白色',
                '雪白','红色','米色',
                '黄色','品蓝','青色',
                '天蓝','黄绿','绿色',
                '紫色','梅红','蓝色',
                '棕色','草绿','橙红']                
    return ColourValue,ColourName
    
ColourValue,ColourName=CreatCommonColourTable()

normalizeddata,ranges,minvals,maxvals=NormalizeData(ColourValue)

print(normalizeddata)
print(ranges)
print(minvals)
print(maxvals)
