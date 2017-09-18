# -*- coding:utf-8 -*-
# Gradient Descent 梯度下降法
# https://ctmakro.github.io/site/on_learning/gd.html
# 已知 x0 * x1 + x0 * x2^2 + x1 + x1^3 + x2 + x2^5 + x3 + x3^7 - 15 = 0, 求 x0, x1, x2和x3.
import numpy as np


def problem(x):
    return x[0] * x[1] + x[0] * (x[2] ** 2) + x[1] + x[1] ** 3 + x[2] + x[2] ** 5 + x[3] + x[3] ** 7 - 15


def error(x):
    return (problem(x) - 0) ** 2


def gradient_descent(x, alpha=0.001):
    delta = 0.00000001
    gradient = np.zeros(x.shape)  # 梯度矢量

    for i in range(len(gradient)):  # 逐个求取偏导数，放进梯度矢量
        deltavector = np.zeros(x.shape)
        deltavector[i] = delta
        gradient[i] = (error(x + deltavector) - error(x - deltavector)) / (delta * 2)

    x = x - gradient * alpha
    return x


def main():
    x = np.array([0.0, 0.0, 0.0, 0.0])
    for i in range(50):
        x = gradient_descent(x, alpha=0.001)
        print('i = {}, x = {}, problem(x) = {:6f}'.format(i, x, problem(x)))


if __name__ == '__main__':
    main()


# 已知 x^3 + 2x + e^x - 3 = 0，求x。

# def problem(x):
#     # return x ** 3 + 2 * x + e ** x - 3
#     return x ** 2 - 3
#
#
# def error(x):
#     return (problem(x) - 0) ** 2
#
#
# def derivative_descent(x):
#     delta = 0.00000001
#     alpha = 0.01
#     derivative = (error(x + delta) - error(x - delta)) / (delta * 2)
#     # error 在 x 处的导数，这里是用导数的定义求的
#     x = x - derivative * alpha
#     return x
#
#
# def main():
#     x = 1
#     # x = 0
#     for i in range(100):
#         x = derivative_descent(x)
#         print('i={}, x = {:6f}, problem(x) = {:6f}'.format(i, x, problem(x)))