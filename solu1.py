# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:11:33 2022

@author: weiqi
"""


def solution(string):
    s = 0
    count = 0
    for i in range(len(string)):
        if string[i] == '>':
            count = count + 1
        if string[i] == '<':
            s = s + count 
    return s*2

