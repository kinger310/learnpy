# --*-- coding=utf-8 --*--
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.context('ggplot2')

from math import radians, cos, sin, asin, sqrt
from random import random, randint


# 参数
m = 31                             # 蚂蚁数量
alpha = 1                          # 信息素重要程度因子
beta = 3                           # 启发函数重要程度因子
vol = 0.2                          # 信息素挥发(volatilization)因子
Q = 10                              # 常系数
iter_max = 500                     # 最大迭代次数
# Heu_F = 1./D                       # 启发函数(heuristic function) η
# Tau = ones(n,n)                    # 信息素矩阵
# Table = zeros(m,n)                 # 路径记录表
# iter = 1                           # 迭代次数初值
# Route_best = zeros(iter_max,n)     # 各代最佳路径
# Length_best = zeros(iter_max,1)    # 各代最佳路径的长度
# Length_ave = zeros(iter_max,1)     # 各代路径的平均长度
# Limit_iter = 0                     # 程序收敛时迭代次数
CAPACITY = 4500

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
    def __init__(self, nodes, alpha=1, beta=3, min_pheromone=0.1, vol=0.2, Q=10):
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


class AntColony(object):
    """
    Ant colony representation
    """
    def __init__(self, m):
        self.ants = []
        self.m = m
        self.shortest_path = None
        self.min_distance = float("inf")

    def reset_ants(self, n, graph):
        # 随机产生蚂蚁的起点城市(一定设在非起始点)
        for _ in range(self.m):
            pos = randint(1, n - 1)
            self.ants.append(Ant(pos, capacity=CAPACITY - graph.amounts[pos]))

    def do_cycles(self, graph):
        n = len(graph.nodes)
        all_nodes = set(range(n))
        self.reset_ants(n, graph)
        # 每个蚂蚁进行路径选择
        for ant in self.ants:
            tabu_set = set(ant.path)
            # ant.capacity -= graph.amounts[ant.path[-1]]
            tabu_set.add(0)
            available = all_nodes - tabu_set
            while available:
                ant.go_to_next(graph, available)
                available = available - set(ant.path)

            graph.local_update_pheromones(passes=ant.get_passes())
            ant.get_distance(graph=graph)

            if self.min_distance > ant.distance:
                self.min_distance = ant.distance
                self.shortest_path = ant.path[:]


class Ant(object):
    def __init__(self, position, capacity):
        self.path = [position]
        self.capacity = capacity
        self.distance = float("inf")

    def go_to_next(self, graph, available):
        # if len(available) == 1:
        #     self.path.append(available.pop())
        if not available:
            return

        total = 0
        probabilities = {}
        for node_index in available:
            probabilities[node_index] = graph.get_probability(self.path[-1], node_index)
            total += probabilities[node_index]
        # q = random()
        # if q <= 0.5:
        #     next_node = max(probabilities, key=lambda x: probabilities[x])
        # else:
        # 轮盘赌法访问下一个节点
        # 随机选择区间choose
        threshold = random()
        probability = 0
        for node_index in available:
            probability += probabilities[node_index] / total
            if threshold < probability:
                # self.path.append(node_index)
                next_node = node_index
                break

        if self.capacity > graph.amounts[next_node]:
            self.capacity -= graph.amounts[next_node]
            self.path.append(next_node)
        else:
            self.capacity = CAPACITY
            self.path.append(0)

            # if 0 in available:
            #     available
            # TODO 选择完毕后，应当选择满足demand量的点
            # TODO 如果满足demand，move to it; 如果不满足，back to start.

    def get_distance(self, graph):
        self.distance = graph.get_path_distance(self.path)

    def get_passes(self):
        path_len = len(self.path)

        return [(self.path[0], 0)] + [
            tuple(sorted((self.path[i], self.path[(i + 1) % path_len]), reverse=True))
            for i in range(path_len)
        ] + [(self.path[0], 0)]

import os
import sys

def main():
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    df_city = pd.read_csv(abspath + r'\data\eil30.csv')
    nodes = [Node(z.x, z.y, z.demand) for z in df_city.itertuples()]
    graph = Graph(nodes=nodes)
    ant_colony = AntColony(m)
    dis_result = []
    dis_result2 = []
    for i in range(iter_max):
        print(i)
        ant_colony.do_cycles(graph)
        graph.update_pheromones(ant_colony)
        min_distance = ant_colony.min_distance
        shortest_path = ant_colony.shortest_path
        dis_result.append(min_distance)
        dis_result2.append((i, min_distance, shortest_path))

    # pd.to_pickle(dis_result2, 'aaa.pkl')
    best_distance = dis_result2[-1][1]
    best_path = dis_result2[-1][2]
    best_path.append(0)
    # best_path = [10, 11, 12, 14, 8, 9, 17, 7, 13, 16, 15, 23, 18, 0, 21, 22, 20, 19, 3, 4, 5, 6, 24, 25, 0, 2, 26, 28, 27, 0, 29, 1, 0]
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
                plt.text(tx, ty+0.5, '({},{})'.format(capacity, demand_t),
                         fontsize=6, color='r', verticalalignment='bottom', horizontalalignment='center')


    plt.figure('fig2')
    plt.plot(dis_result, 'r-')

    plt.show()


    print('ok')





if __name__ == '__main__':
    main()

