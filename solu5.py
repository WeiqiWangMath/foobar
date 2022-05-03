# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:02:05 2022

@author: weiqi
"""

def solution(x,y):
    a = max(int(x),int(y))
    b = min(int(x),int(y))
    num_generation = 0
    while (b != 1 and b != 0):
        num_generation +=  (a // b)
        b1 = a % b
        a = b
        b = b1
    if b == 0 :
        return("impossible")
    else:
        return(num_generation+(a//b)-1)