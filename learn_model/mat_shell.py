import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

import pandas as pd
import os
import sys

from learn_model.aco_mm import Graph

A = 10.5
pause = False


class Node(object):
    """
    构造节点，计算两个节点间的距离
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, node):
        x1, x2, y1, y2 = self.x, node.x, self.y, node.y
        a = int(A)
        if x1 != x2 and (y1 - A) * (y2 - A) > 0:
            if y1 > A:
                y1, y2 = y1 - a, y2 - a
            return abs(x1 - x2) + min(y1 + y2, 2 * a - y1 - y2)
        return abs(x1 - x2) + abs(y1 - y2)

def main():
    filename = sys.argv[0]
    dirname = os.path.dirname(filename)
    abspath = os.path.abspath(dirname)
    # df_city = pd.read_csv(abspath + r'\data\order40.csv')
    # df = df_city.loc[0:10, 'x':'y']
    df = pd.read_csv(abspath + r'\data\steiner.csv')
    df_nodes = df.loc[0:10, :]
    df_st = df.loc[11:, :]
    nodes = [Node(z.x, z.y) for z in df.itertuples()]
    graph = Graph(nodes=nodes)

    nodes1 = [Node(z.x, z.y) for z in df_nodes.itertuples()]
    path_st = get_st_map(df, nodes1)
    best_path = [0, 2, 8, 1, 10, 4, 7, 9, 3, 5, 6]
    real_path = []
    for i in range(len(best_path)):
        node_pair = (best_path[i], best_path[(i+1) % len(best_path)])
        if i == 0:
            real_path = list(path_st[node_pair])
        else:
            real_path += path_st[node_pair][1:]

    fig = plt.figure('fig1')
    ax = fig.add_subplot(111)
    plt.scatter(df_nodes['x'], df_nodes['y'], c='r', s=20)
    sc = plt.scatter(df_st['x'], df_st['y'], s=20)
    i = -1
    for x, y in zip(df['x'], df['y']):
        i += 1
        plt.text(x, y-0.3, i, fontsize=6, verticalalignment='top', horizontalalignment='center')

    for j in range(len(real_path) - 1):
        x, y = df.loc[real_path[j], 'x'], df.loc[real_path[j], 'y']
        tx, ty = df.loc[real_path[j + 1], 'x'], df.loc[real_path[j + 1], 'y']
        plt.annotate('', xy=(x, y), xytext=(tx, ty),
                     arrowprops=dict(arrowstyle="<-", connectionstyle="arc3", color='g'))

    plt.show()

    print('ok')
    #
    # def onClick(event):
    #     global pause
    #     pause ^= True
    # #
    # #
    # def simData():
    #     xy_list = []
    #     for j in range(len(real_path) - 1):
    #         x0, y0 = df.loc[real_path[j], 'x'], df.loc[real_path[j], 'y']
    #         tx, ty = df.loc[real_path[j + 1], 'x'], df.loc[real_path[j + 1], 'y']
    #         xy_list.append((x0, y0, tx, ty))
    #     t_max = 1000.0
    #     dt = 0.01
    #     t = 0.0
    #     while t < t_max:
    #         if not pause:
    #
    #             if x0 == tx and y0
    #             v_x = 0.1 * (tx - x0)
    #             v_y = 0.1 * (ty - y0)
    #             x0 += v_x * t
    #             y0 += v_y * t
    #             yield x0, y0, t
    # #
    # def simPoints(simData):
    #     x, y, t = simData[0], simData[1], simData[2]
    #     time_text.set_text(time_template%(t))
    #     line.set_data(x, y)
    #     return line, time_text
    # #
    #
    # line, = ax.plot([], [], 'bo', ms=10)
    # time_template = 'Time = %.2f s'    # prints running simulation time
    # time_text = ax.text(-0.5, 19.5, '', transform=ax.transAxes)
    # fig.canvas.mpl_connect('button_press_event', onClick)
    # ani = animation.FuncAnimation(fig, simPoints, simData, blit=False, interval=10,
    #     repeat=True)
    # # # ani2 = animation.FuncAnimation(fig, cosPoints, cosData, blit=False, interval=10,
    # # #     repeat=True)
    # # plt.show()


def get_st_map(df, nodes1):
    path_st = {}
    A1 = A + 10
    A0 = A - 10
    for i, node in enumerate(nodes1):
        for j in range(i):
            x1, x2, y1, y2 = node.x, nodes1[j].x, node.y, nodes1[j].y
            if x1 == x2:
                path_st[(i, j)] = (i, j)
                path_st[(j, i)] = (j, i)
            elif x2 == 0:
                x = df[(df['x'] == x1) & (df['y'] == A0)].index[0]
                path_st[(i, j)] = (i, x, j)
                path_st[(j, i)] = (j, x, i)
            elif (y1 - A) * (y2 - A) < 0:
                x = df[(df['x'] == x1) & (df['y'] == A)].index[0]
                y = df[(df['x'] == x2) & (df['y'] == A)].index[0]
                path_st[(i, j)] = (i, x, y, j)
                path_st[(j, i)] = (j, y, x, i)
            elif y1 > A:
                if abs(y1 - A1) + abs(y2 - A1) < y1 + y2 - 2 * A:
                    x = df[(df['x'] == x1) & (df['y'] == A1)].index[0]
                    y = df[(df['x'] == x2) & (df['y'] == A1)].index[0]
                else:
                    x = df[(df['x'] == x1) & (df['y'] == A)].index[0]
                    y = df[(df['x'] == x2) & (df['y'] == A)].index[0]
                path_st[(i, j)] = (i, x, y, j)
                path_st[(j, i)] = (j, y, x, i)
            else:
                if abs(y1 - A0) + abs(y2 - A0) < y1 + y2 - 2 * A:
                    x = df[(df['x'] == x1) & (df['y'] == A0)].index[0]
                    y = df[(df['x'] == x2) & (df['y'] == A0)].index[0]
                else:
                    x = df[(df['x'] == x1) & (df['y'] == A)].index[0]
                    y = df[(df['x'] == x2) & (df['y'] == A)].index[0]
                path_st[(i, j)] = (i, x, y, j)
                path_st[(j, i)] = (j, y, x, i)
    return path_st


if __name__ == '__main__':
    main()


    # def cosData():
    #     t_max = 10.0
    #     dt = 0.01
    #     x = 0.0
    #     t = 0.0
    #     while t < t_max:
    #         if not pause:
    #             x = np.cos(np.pi * t)
    #             t = t + dt
    #         yield x, t
    #
    #
    # def cosPoints(cosData):
    #     x, t = cosData[0], cosData[1]
    #     # time_text.set_text(time_template%(t))
    #     line2.set_data(t, x)
    #     return line2