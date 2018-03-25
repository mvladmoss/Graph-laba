import os
import operator
import sys
import time
from threading import Thread
import threading
timer = 0
start_time = time.time()
sys.setrecursionlimit(2**20)
result = []
data = []
points = []
with open("12.in") as f:
    for line in f:
        data.append([int(x) for x in line.split()])  
        # Считываю кол-во вершин и ребер, а затем пары чисел и записываю в их 
        # в виде списка из 2 элементов в список data
number_of_point = (int(data[0][0]))
number_of_edge = (int(data[1][0]))
n = number_of_point
fup = [0 for i in range(number_of_point + 1)]
tin = [0 for i in range(number_of_point + 1)]
used = [False for i in range(number_of_point + 1)]
matrica = [[] for i in range(number_of_point + 1)]
dic1 = dict()
dic2 = dict()
dic3 = dict()
dic4 = dict()
for i in range(2, number_of_edge + 2):
    if data[i][1] not in matrica[data[i][0]]:  
        matrica[data[i][0]].append(data[i][1])
    if data[i][0] not in matrica[data[i][1]]:
        matrica[data[i][1]].append(data[i][0])
    f = tuple(data[i])
    q = (data[i][1], data[i][0])
    if f or q not in dic1:
        dic3[f] = True
        dic4[q] = True
    else:
        dic3[f] = False
        dic4[q] = False
    dic1[i - 1] = f
    k = (data[i][0], data[i][1])
    dic2[k] = i - 1


def main():
    print(len(result))
    result.sort()
    print(result)
    print(len(points))
    points.sort()
    print(points)
    print("--- %s seconds ---" % (time.time() - start_time))


def dfs(v, p=-1):
    used[v] = True
    global timer
    temp_time = timer
    tin[v] = temp_time
    fup[v] = temp_time
    timer += 1
    children = 0
    for i in range(0, len(matrica[v])):
        to = matrica[v][i]
        if to == p:
            continue
        if used[to]:
                fup[v] = min(fup[v], tin[to])
        else:
            dfs(to, v)
            fup[v] = min(fup[v], fup[to])
            if (fup[to] >= tin[v] and p != -1):
                IS_CUTPOINT(v)
            children = children + 1    
            if (fup[to] > tin[v]):
                IS_BRIDGE(v, to)
    if p == -1 and children > 1:
        IS_CUTPOINT(v)            


def IS_CUTPOINT(v):
    if v not in points:
        points.append(v)


def find_bridges1():
    for i in range(1, (n + 1)):
        if not used[i]:
            dfs(i)


def IS_BRIDGE(s1, s2):
    temp1 = (s1, s2)
    temp2 = (s2, s1)
    if temp1 in dic1.values():
        if dic3.get(temp1) or dic4.get(temp1):
            k = (dic2.get(temp1))
            result.append(k)
                
    else:
        if dic3.get(temp2) or dic4.get(temp2):
            k = (dic2.get(temp2))
            result.append(k)


threading.stack_size(67108864 // 8)
thread = threading.Thread(target=find_bridges1)
thread.start()
thread.join()
main()







