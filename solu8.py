# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:02:05 2022

@author: weiqi
"""

def solution(current_state):
    w = len(current_state[0])
    h = len(current_state)
    s = [[1] for i in range(2**(h+1))]
    bit_array = [[] for j in range(2**(h+1))]
    for j in range(2**(h+1)):
        j1 = j
        for l in range(h+1):
            bit_array[j].append(j1 & 1)
            j1 = j1 >> 1
    for i in range(1,w+1):
        for j in range(2**(h+1)):
            s[j].append(0)
        for j in range(2**(h+1)):
            for k in range(2**(h+1)):
                j1 = j
                k1 = k
                j_array = []
                k_array = []
                flag = True
                j_array = bit_array[j]
                k_array = bit_array[k]
                for l in range(h):
                    if current_state[l][i-1]:
                        if j_array[l] + j_array[l+1] + k_array[l] + k_array[l+1] != 1:
                            flag = False
                            break
                    else:
                        if j_array[l] + j_array[l+1] + k_array[l] + k_array[l+1] == 1:
                            flag = False
                            break
                if flag:
                    s[k][i] += s[j][i-1]
    num_previous_state = 0
    for j in range(2**(h+1)):
        num_previous_state += s[j][w]
    return(num_previous_state)                    
    