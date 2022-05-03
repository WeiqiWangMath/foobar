# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:11:33 2022

@author: weiqi
"""


def solution(version_list):
    version_list_sorted = version_list
    for i in range(len(version_list)-1):
        for j in range(i+1,len(version_list)):
            if is_greater(version_list_sorted[i],version_list_sorted[j]):
                temp = version_list_sorted[i]
                version_list_sorted[i] = version_list_sorted[j]
                version_list_sorted[j] = temp
    return version_list_sorted


def is_greater(string1,string2):
    string_temp = string1
    A=[]
    while string_temp.find('.')>=0:
        A.append(int(string_temp[0:string_temp.find('.')]))
        string_temp = string_temp[(string_temp.find('.')+1):]
    A.append(int(string_temp))
    string_temp = string2
    B=[]
    while string_temp.find('.')>=0:
        B.append(int(string_temp[0:string_temp.find('.')]))
        string_temp = string_temp[(1+string_temp.find('.')):]
    B.append(int(string_temp))
    return A>B

