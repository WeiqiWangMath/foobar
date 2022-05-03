# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:02:05 2022

@author: weiqi
"""

def solution(num_bun,num_require):
    A = [[] for i in range(num_bun)]
    count = 0
    for k in range(2**num_bun):
       k_num = k
       bit_k = []
       for i in range(num_bun):
           bit_k.append(k_num & 1)
           k_num = k_num >> 1
       if sum(bit_k) == num_require - 1 :
           for i in range(num_bun):
               if bit_k[num_bun-i-1] == 0:
                   A[i].append(count)
           count += 1
    return A