# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:46:06 2022

@author: weiqi
"""

def solution(map_maze):
    l = len(map_maze)
    w = len(map_maze[0])
    min_step = [[[99999 for i in range(w)] for j in range(l)]for k in range(2)]
    block_flag = [0]
    x = [0]
    y = [0]
    min_step[0][0][0] = 1
    min_step[1][0][0] = 1
    l_list = 1
    num_step = 1
    while l_list>0:
        num_step += 1
        x1 = []
        y1 = []
        block_flag1 = []
        for i in range(l_list):
            if x[i]+1 < l:
                if (map_maze[x[i]+1][y[i]] == 0 \
                and num_step < min_step[block_flag[i]][x[i]+1][y[i]]):
                    x1.append(x[i]+1)
                    y1.append(y[i])
                    block_flag1.append(block_flag[i])
                    min_step[block_flag[i]][x[i]+1][y[i]] = num_step
                if (map_maze[x[i]+1][y[i]] == 1 and block_flag[i] == 0 
                and num_step < min_step[1][x[i]+1][y[i]]):
                    x1.append(x[i]+1)
                    y1.append(y[i])
                    block_flag1.append(1)
                    min_step[1][x[i]+1][y[i]] = num_step
            if x[i]-1 >= 0:
                if (map_maze[x[i]-1][y[i]] == 0  
                and num_step < min_step[block_flag[i]][x[i]-1][y[i]]):
                    x1.append(x[i]-1)
                    y1.append(y[i])
                    block_flag1.append(block_flag[i])
                    min_step[block_flag[i]][x[i]-1][y[i]] = num_step
                if (map_maze[x[i]-1][y[i]] == 1 and block_flag[i] == 0 
                and num_step < min_step[1][x[i]-1][y[i]]):
                    x1.append(x[i]-1)
                    y1.append(y[i])
                    block_flag1.append(1)
                    min_step[1][x[i]-1][y[i]] = num_step
            if y[i]+1 < w:
                if (map_maze[x[i]][y[i]+1] == 0  
                and num_step < min_step[block_flag[i]][x[i]][y[i]+1]):
                    x1.append(x[i])
                    y1.append(y[i]+1)
                    block_flag1.append(block_flag[i])
                    min_step[block_flag[i]][x[i]][y[i]+1] = num_step
                if (map_maze[x[i]][y[i]+1] == 1 and block_flag[i] == 0 
                and num_step < min_step[1][x[i]][y[i]+1]):
                    x1.append(x[i])
                    y1.append(y[i]+1)
                    block_flag1.append(1)
                    min_step[1][x[i]][y[i]+1] = num_step
            if y[i]-1 >= 0:
                if (map_maze[x[i]][y[i]-1] == 0 
                and num_step < min_step[block_flag[i]][x[i]][y[i]-1]):
                    x1.append(x[i])
                    y1.append(y[i]-1)
                    block_flag1.append(block_flag[i])
                    min_step[block_flag[i]][x[i]][y[i]-1] = num_step
                if (map_maze[x[i]][y[i]-1] == 1 and block_flag[i] == 0 
                and num_step < min_step[1][x[i]][y[i]-1]):
                    x1.append(x[i])
                    y1.append(y[i]-1)
                    block_flag1.append(1)
                    min_step[1][x[i]][y[i]-1] = num_step
        x = x1
        y = y1
        block_flag = block_flag1
        l_list = len(x)
    return min(min_step[0][l-1][w-1],min_step[1][l-1][w-1])