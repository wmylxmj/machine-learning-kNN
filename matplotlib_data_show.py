# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:12:55 2018
@author: wmy
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy

'''画出图纸'''
fig=plt.figure()
ax=fig.add_subplot(111)

def CreatTestTable():
    x=50
    y=100
    z=150
    value=numpy.array([[3,2],[4,5],[2.1,3.4],
                 [1.2,0],[5.7,3.2],[9.4,10],
                 [4.1,9.8],[2.2,8.7],[8.7,1.1],
                 [5,5],[9.8,9.8],[5.8,5.4],
                 [5.5,0.1],[2.4,2.4],[7.2,2.3],
                 [7.8,8.7],[4.4,8.7],[8,7],
                 [2.3,5.6],[8.9,6.7],[4.2,4.2],
                 [6,8.3],[6.9,8.1],[7.9,1.1],
                 [8.1,4.5],[4.3,4.3],[6.5,4.2],
                 [4,2],[4,9.8],[1.5,4.4]])
    labels=[x,y,y,
            x,x,y,
            y,y,x,
            z,z,x,
            x,z,x,
            y,y,x,
            y,x,z,
            y,y,x,
            x,z,x,
            x,y,y]
    return value,labels

value,labels=CreatTestTable()

#维数
#ax.scatter(value[:,0],value[:,1])
ax.scatter(value[:,0],value[:,1],
           numpy.array(labels),numpy.array(labels))
plt.show()
