# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 09:57:44 2022

@author: weiqi
"""

def solution(list_num):
    n = len(list_num)
    luck_count = [[0 for i in range(n)] for j in range(2)]
    for i in range(1,n):
        for j in range(i):
            if list_num[i] % list_num[j] == 0:
                luck_count[0][i] += 1
                luck_count[1][i] += luck_count[0][j]
    return sum(luck_count[1])