# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:02:05 2022

@author: weiqi
"""

def solution(map_vertex,time_limit):
    n = len(map_vertex)
    if negative_cycle(map_vertex):
        return([i for i in range(n-2)])
    vertex_visited = [1]
    current_vertex = [0]
    Best_time = [[99999 for i in range(2**n)]for j in range(n)]
    Best_time[0][1] = 0
    while len(current_vertex)>0:
        for i in range(n):
            if Best_time[i][vertex_visited[0] | 2**i] > Best_time[current_vertex[0]][vertex_visited[0]] + map_vertex[current_vertex[0]][i]:
                Best_time[i][vertex_visited[0] | 2**i] = Best_time[current_vertex[0]][vertex_visited[0]] + map_vertex[current_vertex[0]][i]
                vertex_visited.append(vertex_visited[0] | 2**i)
                current_vertex.append(i)
        vertex_visited.remove(vertex_visited[0])
        current_vertex.remove(current_vertex[0])
    Best_num_bunny = 0
    Bunny_list = []
    for i in range(2**n):
        if Best_time[n-1][i] <= time_limit:
            count = 0
            for j in range(1,n-1):
                if (i & (2**j)) > 0:
                    count += 1
            if count > Best_num_bunny:
                Bunny_list = []
                for j in range(1,n-1):
                    if (i & (2**j)) > 0:
                        Bunny_list.append(j-1)
                Best_num_bunny = count
    return Bunny_list
def negative_cycle(map_vertex):
    n = len(map_vertex)
    d = [99999 for i in range(n)]
    d[0] = 0
    count_inQ = [0 for i in range(n)]
    Q = [0]
    count_inQ[0] = 1
    while len(Q)>0:
        for i in range(n):
            if d[i] > d[Q[0]] + map_vertex[Q[0]][i]:
                d[i] = d[Q[0]] + map_vertex[Q[0]][i]
                if Q.count(i) == 0:
                    Q.append(i)
                    count_inQ[i] += 1
                    if count_inQ[i] == n:
                        return True
        Q.remove(Q[0])
    return False