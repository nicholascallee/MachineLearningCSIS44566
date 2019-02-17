# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 12:06:17 2019

@author: S516583
"""

import numpy as np
num = 0
e = 2.7182818284590452353602874713527
x = [1,1,2,4,5,7,10,14,15,16]
avgLoss1 =0
avgLoss2 =0
def function1 (x):
    return (pow(e,2*(x-3)))/(1+pow(e,2*(x-3)))

def function2 (x):
    return (pow(e,2*(x-6)))/(1+pow(e,2*(x-6)))
def logLoss(p):
    if (p > .5):
        return -(1*np.log(p))
    else:
        return -(np.log(1-p))


print("function1")
for b in range(0,10):
    
    print("x is: " + str(x[b]))
    
    if (function1(x[b]) >.5):
        print(function1(x[b]))
        print("log loss: " + str(logLoss(function1(x[b]))))
        avgLoss1 += logLoss(function1(x[b]))
        print("blue")
    else:
        print(function1(x[b]))
        print("log loss: " + str(logLoss(function1(x[b]))))
        avgLoss1 += logLoss(function1(x[b]))
        print("red")

avgLoss1 = avgLoss1 / 9
print ("average log loss fn1: " + str(avgLoss1))
print("*******************************************************************************************")
print("function2")
for b in range(0,10):
    
    print("x is: " + str(x[b]))
    
    if (function2(x[b]) >.5):
        print(function2(x[b]))
        print("log loss: " + str(logLoss(function2(x[b]))))
        avgLoss2 += logLoss(function2(x[b]))
        print("blue")
    else:
        print(function2(x[b]))
        print("log loss: " + str(logLoss(function2(x[b]))))
        avgLoss2 += logLoss(function2(x[b]))
        print("red")
avgLoss2 = avgLoss2 / 9
print ("average log loss fn2: " + str(avgLoss2))