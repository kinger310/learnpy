# """
# 绘制多个子图
# 一个Figure对象可以包含多个子图（Axes），在matplotlib中用Axes对象表示一个绘图区域，称为子图，可以使用subplot()快速绘制包含多个子图的图表，它的调用形式如下：
# subplot(numRows,numCols,plotNum)
# 图表的整个绘图区域被等分为numRows行和numCols列，然后按照从左到下的顺序对每个区域进行编号，左上区域的编号为1。plotNum参数指定创建的Axes对象所在的区域
# """
# import numpy as np
# import matplotlib.pyplot as plt
# plt.figure(1)#创建图表1
# plt.figure(2)#创建图表2
# ax1=plt.subplot(211)#在图表2中创建子图1
# ax2=plt.subplot(212)#在图表2中创建子图2
# x=np.linspace(0,3,100)
# for i in range(5):
#     plt.figure(1)
#     plt.plot(x,np.exp(i*x/3))
#     plt.sca(ax1)
#     plt.plot(x,np.sin(i*x))
#     plt.sca(ax2)
#     plt.plot(x,np.cos(i*x))
# plt.show()


# --*-- coding=utf-8 --*--
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
import sys

plt.style.context('ggplot2')

from math import radians, cos, sin, asin, sqrt
from random import random, randint


class Node(object):
    """
    构造节点，计算两个节点间的距离
    """
    def __init__(self, x, y, demand):
        self.x = x
        self.y = y
        self.demand = demand

    def distance(self, node):
        return sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)




class Graph(object):
    """
    由节点构造图，涉及图的节点距离、总距离等信息
    """
    def __init__(self, nodes, alpha=1, beta=3, min_pheromone=0.01, vol=0.2, Q=10):
        self.nodes = nodes
        self.alpha = alpha
        self.beta = beta
        self.min_pheromone = min_pheromone
        self.vol = vol
        self.Q = Q
        self._distances = {}
        self._pheromones = {}
        self._deposit = {}
        self.total_distance = 0
        self.amounts = {}
        for i, node in enumerate(self.nodes):
            self.amounts[i] = node.demand
            for j in range(i):
                distance = node.distance(self.nodes[j])
                self._distances[(i, j)] = distance
                self.total_distance += distance
                self._pheromones[(i, j)] = min_pheromone
                self._deposit[(i, j)] = Q / distance

    def _get_distance(self, i, j):
        return self._distances.get((i, j)) or self._distances.get((j, i))

    def get_path_distance(self, path):
        distance = 0
        path1 = path.copy()
        path1.append(0)
        idxs = [i for i, j in enumerate(path1) if j == 0]
        lists = []
        for k, idx in enumerate(idxs):
            if k == 0:
                a_list = [0] + path1[:idx + 1]
            else:
                a_list = [0] + path1[idxs[k - 1] + 1:idx + 1]
            lists.append(a_list)
        for p in lists:
            for i in range(len(p) - 1):
                distance += self._get_distance(p[i], p[i+1])
        return distance

    def heu_dis_fun(self, i, j):
        return self._get_distance(i, j) ** -1

    def get_pheromone(self, i, j):
        return self._pheromones.get((i, j), 0) or self._pheromones.get((j, i), 0)

    def get_probability(self, i, j):
        """
        Returns probability of going from ith node to the jth
        """
        return (
            (self.get_pheromone(i, j) ** self.alpha) *
            (self.heu_dis_fun(i, j) ** self.beta)
        )

    def update_pheromones(self, ant_colony):
        """
        Updates pheromones between nodes globally
        """
        min_distance = ant_colony.min_distance
        for node_pair in self._pheromones:
            self._pheromones[node_pair] *= (1 - self.vol)
        for ant in ant_colony.ants:
            distance = self.get_path_distance(ant.path)
            if distance <= 1.1 * min_distance:
                for node_pair in ant.get_passes():
                    self._pheromones[node_pair] += self.Q / ant.distance

    def local_update_pheromones(self, passes):
        n = len(self.nodes)
        L_nn = min(self._distances.values())
        for i, j in passes:
            self._pheromones[(i, j)] *= (1 - self.vol)
            self._pheromones[(i, j)] += self.vol / (n * L_nn)


filename = sys.argv[0]
dirname = os.path.dirname(filename)
abspath = os.path.abspath(dirname)
df_city = pd.read_csv(abspath + r'\data\eil30.csv')
nodes = [Node(z.x, z.y, z.demand) for z in df_city.itertuples()]
graph = Graph(nodes=nodes)

best_path = [18, 23, 10, 11, 12, 8, 14, 9, 17, 7, 13, 16, 15, 0, 19, 6, 1, 24, 25, 29, 27, 28, 26, 0, 20, 3, 4, 5, 2, 22, 0, 21]
best_distance = graph.get_path_distance(best_path)
best_path.append(0)

plt.figure('fig1')
sc = plt.scatter(df_city['x'], df_city['y'], s=20)
i = -1
for x, y in zip(df_city['x'], df_city['y']):
    i += 1
    plt.text(x, y-1, i, fontsize=6, verticalalignment='top', horizontalalignment='center')
plt.title('min distance = {:2f}'.format(best_distance))
idxs = [i for i, j in enumerate(best_path) if j == 0]
lists = []
for k, idx in enumerate(idxs):
    if k == 0:
        a_list = [0] + best_path[:idx + 1]
    else:
        a_list = [0] + best_path[idxs[k - 1] + 1:idx + 1]
    lists.append(a_list)
l = -1
for fig_list in lists:
    c_list = ['b', 'g', 'y', 'm', 'k']
    l += 1
    capacity = 4500
    for j in range(len(fig_list) - 1):
        demand = df_city.loc[fig_list[j], 'demand']
        capacity = capacity - demand
        demand_t = df_city.loc[fig_list[j+1], 'demand']
        x, y = df_city.loc[fig_list[j], 'x'], df_city.loc[fig_list[j], 'y']
        tx, ty = df_city.loc[fig_list[j+1], 'x'], df_city.loc[fig_list[j+1], 'y']
        plt.annotate('', xy=(x, y), xytext=(tx, ty), arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color=c_list[l]))
        if j < len(fig_list) - 2:
            plt.text(tx, ty+0.5, '{},{}'.format(capacity, demand_t),
                     fontsize=6, color='r', verticalalignment='bottom', horizontalalignment='center')
plt.show()
print('ok')
