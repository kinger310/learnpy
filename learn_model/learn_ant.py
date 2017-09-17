from ant_colony.graph import Node, Graph
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.context('ggplot2')

from math import radians, cos, sin, asin, sqrt


def haversine(lat1, lon1, lat2, lon2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
    """ 
    Calculate the great circle distance between two points  
    on the earth (specified in decimal degrees) 
    """
    # 将十进制度数转化为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = abs(lon2 - lon1)
    dlat = abs(lat2 - lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # 地球平均半径，单位为公里
    return c * r


df = pd.read_csv(r'D:\ProgramFiles\PycharmProjects\learnpy\learnscrapy\week9\burma14.csv')

fig1 = plt.figure()
sc = plt.scatter(df['x'], df['y'])
i = -1
for x, y in zip(df['x'], df['y']):
    i += 1
    plt.annotate(
        '({0})'.format(i),
        xy=(x, y),
        xytext=(0, -5),
        textcoords='offset points',
        xycoords='data',
        ha='center',
        va='top')
nodes = [Node(z.x, z.y) for z in df.itertuples()]
graph = Graph(nodes, alpha=1, beta=5, decay=0.2)
# path, distance = graph.find_shortest_path(n=1, m=28)
d_list = []
n_list = list(range(0, 1001, 10))
shortest = 100000
for n in n_list:
    path, distance = graph.find_shortest_path(n=n, m=21)
    if distance < shortest:
        shortest = distance
        path_shortest = path
    d_list.append(distance)
fig2 = plt.figure()
plt.plot(n_list, d_list, 'r-')

sum = 0
for i in range(len(path_shortest) - 1):
    x1, y1 = df.loc[path_shortest[i]]
    x2, y2 = df.loc[path_shortest[i + 1]]
    real_dis = haversine(x1, y1, x2, y2)
    sum += real_dis
x0, y0 = df.loc[path_shortest[0]]
xn, yn = df.loc[path_shortest[-1]]
sum += haversine(x0, y0, xn, yn)

