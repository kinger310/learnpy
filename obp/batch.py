# -*- coding: utf-8 -*-

import numpy as np
from obp.opt_best import opt_best


def s_shape(df):
    h_unit = 5
    v_unit = 40
    aisle_lst = sorted(set(df['aisle']))
    if aisle_lst:
        max_a = max(aisle_lst)
        num_a = len(aisle_lst)
        if num_a % 2 != 0:
            pos = max(df[df['aisle'] == max_a]['position'])
            travel = 2 + (max_a - 1) * h_unit * 2 + (num_a - 1) * v_unit + pos * 2
        else:
            travel = 2 + (max_a - 1) * h_unit * 2 + num_a * v_unit
    else:
        travel = 0
    return travel


class Batch(object):
    def __init__(self, b, sd=0, pt=0, weight=0, orders=None):
        self.b = b
        self.sd = sd
        self.pt = pt
        self.weight = weight
        self.orders = orders

    def routing_time(self, df_items, para='s'):
        batch_orders = df_items[df_items['order'].isin(self.orders)]
        num_item = len(batch_orders)
        if para == 's':
            travel = s_shape(batch_orders)  # 可以改进成启发式策略？？
        else:
            travel = opt_best(batch_orders)
        if travel == 0:
            self.pt = 0
        else:
            self.pt = 3 + num_item / 4 + travel / 20

    def _routing(self, df_orders):
        self.pt = sum(df_orders.loc[self.orders, 'pt']) - 3 * (len(self.orders) - 1)

    def get_center(self, df_items):
        batch_orders = df_items[df_items['order'].isin(self.orders)]
        center = (np.mean(batch_orders['aisle']), np.mean(batch_orders['position']))
        return center

    def delete(self, order, weight):
        self.orders.remove(order)
        self.weight -= weight

    def add(self, order, weight):
        self.orders.append(order)
        self.weight += weight

    def shift(self, order, weight, batch):
        self.delete(order, weight)
        batch.add(order, weight)

    def swap(self, order1, order2, w1, w2, batch):
        self.delete(order1, w1)
        self.add(order2, w2)
        batch.delete(order2, w2)
        batch.add(order1, w1)

