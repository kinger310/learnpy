# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:47:57 2017

@author: 燃烧杯
"""

import numpy as np
import matplotlib.pyplot as plt

#在这里设置迭代停止条件，要多尝试一些不同数值，最好设置大一点
MAXCOUNT = 100

#数据在这里输入，依次键入每个城市的坐标
cities = np.array([
        [256, 121],
        [264, 715],
        [225, 605],
        [168, 538],
        [210, 455],
        [120, 400],
        [96, 304],
        [10,451],
        [162, 660],
        [110, 561],
        [105, 473]
        ])

def calDist(xindex, yindex):
    return (np.sum(np.power(cities[xindex] - cities[yindex], 2))) ** 0.5

def calPathDist(indexList):
    sum = 0.0
    for i in range(1, len(indexList)):
        sum += calDist(indexList[i], indexList[i - 1])
    return sum

#path1长度比path2短则返回true
def pathCompare(path1, path2):
    if calPathDist(path1) <= calPathDist(path2):
        return True
    return False

def generateRandomPath(bestPath):
    a = np.random.randint(len(bestPath))
    while True:
        b = np.random.randint(len(bestPath))
        if np.abs(a - b) > 1:
            break
    if a > b:
        return b, a, bestPath[b:a+1]
    else:
        return a, b, bestPath[a:b+1]

def reversePath(path):
    rePath = path.copy()
    rePath[1:-1] = rePath[-2:0:-1]
    return rePath

def updateBestPath(bestPath):
    count = 0
    while count < MAXCOUNT:
        print(calPathDist(bestPath))
        print(bestPath.tolist())
        start, end, path = generateRandomPath(bestPath)
        rePath = reversePath(path)
        if pathCompare(path, rePath):
            count += 1
            continue
        else:
            count = 0
            bestPath[start:end+1] = rePath
    return bestPath


def draw(bestPath):
    ax = plt.subplot(111, aspect='equal')
    ax.plot(cities[:, 0], cities[:, 1], 'x', color='blue')
    for i,city in enumerate(cities):
        ax.text(city[0], city[1], str(i))
    ax.plot(cities[bestPath, 0], cities[bestPath, 1], color='red')
    plt.show()

def opt2():
    #随便选择一条可行路径
    bestPath = np.arange(0, len(cities))
    bestPath = np.append(bestPath, 0)
    bestPath = updateBestPath(bestPath)
    draw(bestPath)

opt2()
