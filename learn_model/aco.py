import pandas as pd
import numpy as np

from math import radians, cos, sin, asin, sqrt
from random import random, randint


# 参数
m = 31                             # 蚂蚁数量
alpha = 1                          # 信息素重要程度因子
beta = 5                           # 启发函数重要程度因子
vol = 0.2                          # 信息素挥发(volatilization)因子
Q = 10                              # 常系数
iter_max = 50                     # 最大迭代次数
# Heu_F = 1./D                       # 启发函数(heuristic function) η
# Tau = ones(n,n)                    # 信息素矩阵
# Table = zeros(m,n)                 # 路径记录表
# iter = 1                           # 迭代次数初值
# Route_best = zeros(iter_max,n)     # 各代最佳路径
# Length_best = zeros(iter_max,1)    # 各代最佳路径的长度
# Length_ave = zeros(iter_max,1)     # 各代路径的平均长度
# Limit_iter = 0                     # 程序收敛时迭代次数


class Node(object):
    """
    构造节点，计算两个节点间的距离
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, node):
        return sqrt((self.x - node.x) ** 2 + (self.y - node.y) ** 2)


class Graph(object):
    """
    由节点构造图，涉及图的节点距离、总距离等信息
    """
    def __init__(self, nodes, alpha=1, beta=5, min_pheromone=0.01, vol=0.2, Q=10):
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
        for i, node in enumerate(self.nodes):
            for j in range(i):
                distance = node.distance(self.nodes[j])
                self._distances[(i, j)] = distance
                self._distances[(j, i)] = distance
                self.total_distance += distance
                self._pheromones[(i, j)] = min_pheromone

    def _get_distance(self, i, j):
        return self._distances.get((i, j)) or self._distances.get((j, i))

    def get_path_distance(self, path):
        distance = 0
        path_len = len(path)
        for i in range(path_len):
            distance += self._get_distance(path[i], path[(i + 1) % path_len])
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
        for node_pair in self._pheromones:
            self._pheromones[node_pair] *= (1 - self.vol)
        for ant in ant_colony.ants:
            distance = self.get_path_distance(ant.path)
            if distance <= ant_colony.min_distance:
                for node_pair in ant.get_passes():
                    self._pheromones[node_pair] += self.Q / ant.distance
        for node_pair in self._pheromones:
            self._pheromones[node_pair] = max(
                self._pheromones[node_pair], self.min_pheromone
            )

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

    def reset_ants(self, n):
        # 随机产生蚂蚁的起点城市
        for _ in range(self.m):
            self.ants.append(Ant(randint(0, n - 1)))

    def do_cycles(self, graph):
        n = len(graph.nodes)
        all_nodes = set(range(n))
        self.reset_ants(n)
        # 每个蚂蚁进行路径选择
        for ant in self.ants:
            tabu_set = set(ant.path)
            available = all_nodes - tabu_set
            counter = 0
            while available:
                counter += 1
                ant.go_to_next(graph, available)
                available = all_nodes - set(ant.path)

            graph.local_update_pheromones(passes=ant.get_passes())
            ant.get_distance(graph=graph)

            if self.min_distance > ant.distance:
                self.min_distance = ant.distance
                self.shortest_path = ant.path[:]


class Ant(object):
    def __init__(self, position=0):
        self.path = [position]
        self.distance = float("inf")

    def go_to_next(self, graph, available):
        if len(available) == 1:
            self.path.append(available.pop())

        if not available:
            return

        total = 0
        probabilities = {}
        for node_index in available:
            probabilities[node_index] = graph.get_probability(self.path[-1], node_index)
            total += probabilities[node_index]
        # 轮盘赌法访问下一个节点
        threshold = random()
        probability = 0
        for node_index in available:
            probability += probabilities[node_index] / total
            if threshold < probability:
                self.path.append(node_index)
                return
        self.path.append(available.pop())

    def get_distance(self, graph):
        self.distance = graph.get_path_distance(self.path)

    def get_passes(self):
        path_len = len(self.path)
        return [
            tuple(sorted((self.path[i], self.path[(i + 1) % path_len]), reverse=True))
            for i in range(path_len)
        ]


def main():
    df_city = pd.read_excel(r'E:\PycharmProjects\learnpy\learn_model\data\Chap9_citys_data.xlsx', sheetname='Sheet2')
    nodes = [Node(z.x, z.y) for z in df_city.itertuples()]
    graph = Graph(nodes=nodes, beta=5, vol=0.001, Q=10)
    ant_colony = AntColony(m)
    dis_result = []
    for i in range(iter_max):
        ant_colony.do_cycles(graph)
        graph.update_pheromones(ant_colony)
        min_distance = ant_colony.min_distance
        shortest_path = ant_colony.shortest_path
        dis_result.append((i, min_distance, shortest_path))

    # pd.to_pickle(dis_result, 'aaa.pkl')
    print('ok')



if __name__ == '__main__':
    main()


# import pickle
#
# with open(r'E:\PycharmProjects\learnpy\learn_model\aaa.pkl', 'rb') as file:
#     pickle.load(file)
