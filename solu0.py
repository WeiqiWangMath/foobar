# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:11:33 2022

@author: weiqi
"""


def solution(i):
    j = 2
    len_string = 0
    string_prime = ''
    while len_string <= i+5:
        if is_prime(j):
            string_prime = string_prime + str(j)
            len_string = len_string + len(str(j))
        j = j + 1
    return string_prime[i:i+5]

def is_prime(n):
    for j in range(2,round(n**0.5)+1):
        if n % j == 0 :
            return False
    return True