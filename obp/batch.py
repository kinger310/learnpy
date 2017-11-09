# -*- coding: utf-8 -*-

import numpy as np


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

    def routing_time(self, df_items, strategy='s'):
        batch_orders = df_items[df_items['order'].isin(self.orders)]
        num_item = len(batch_orders)
        if strategy == 's':
            travel = s_shape(batch_orders)
        else:
            travel = 0
        if travel == 0:
            self.pt = 0
        else:
            self.pt = 3 + num_item / 4 + travel / 20

    def get_center(self, df_items):
        batch_orders = df_items[df_items['order'].isin(self.orders)]
        center = (np.mean(batch_orders['aisle']), np.mean(batch_orders['position']))
        return center

    def shift(self, order, weight, batch):
        if order in self.orders:
            self.orders.remove(order)
            self.weight -= weight
            batch.orders.append(order)
            batch.weight += weight
        else:
            return 0

    def swap(self, order1, order2, w1, w2, batch):
        if order1 in self.orders and order2 in batch.orders:
            self.orders.remove(order1)
            self.orders.append(order2)
            self.weight = self.weight - w1 + w2
            batch.orders.remove(order2)
            batch.orders.append(order1)
            batch.weight = batch.weight - w2 + w1
        else:
            return 0

