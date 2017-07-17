# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from math import *


def cloud_transform(y_spor, N):
    '''
    % x 表示云滴
    % y 表示隶属度（这里是“钟形”隶属度），意义是度量倾向的稳定程度
    % Ex 云模型的数字特征，表示期望
    % En 云模型的数字特征，表示熵
    % He 云模型的数字特征，表示超熵
    :param y_spor:
    :param N:
    :return:
    '''
    x = []
    y = []
    Ex = np.mean(y_spor)
    En = np.mean(abs(y_spor - Ex) * sqrt(pi / 2))
    He = sqrt(np.var(y_spor, ddof=1) - pow(En, 2))  # 这里计算样本标准偏差的方差
    for i in range(N):
        Enn = np.random.normal() * He + En
        x1 = np.random.normal() * Enn + Ex
        y1 = exp(- pow((x1 - Ex), 2) / (2 * pow(Enn, 2)))
        x.append(x1)
        y.append(y1)
    return x, y, Ex, En, He


def main():
    # 每幅图生成N个云滴
    N = 1500
    # 射击成绩原始数据，这里数据按列存储所以要转置
    Y = '9.5 10.3 10.1 8.1 10.3 9.7 10.4 10.1 10.6 8.6 9.2 10.0' \
        ' 10.5 10.4 10.1 10.1 10.9 9.8 10.0 10.1 10.6 9.8 9.7 10.0' \
        ' 10.4 10.5 10.6 10.3 10.1 10.2 10.8 8.4 9.3 10.2 9.6 10.0 10.5 10.0 10.7 9.9'
    train = []
    temp = []
    for i, x in enumerate(Y.split()):
        temp.append(float(x))
        if i % 4 == 3:
            train.append(temp)
            temp = []
    np_train = np.array(train)
    x = np.arange(8, 12, 0.1)
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
    for ax, cnt in zip(axes.ravel(), range(4)):
        # ax.set_title('No. %d cloud model' % (cnt+1))
        x, y, Ex, En, He = cloud_transform(np_train[:, cnt], N)
        ax.plot(x, y, 'r.')
        ax.set_xlabel('target')
        ax.set_ylabel('confidence')
        ax.set_xlim([8, 12])
        ax.set_ylim([0, 1])
        print('No {0}, expectation= {1}, Entropy= {2}, Hypo-entropy= {3}, points= {4}'
              .format((cnt+1), Ex, En, He, Ex / (En+He)))
    plt.show()

if __name__ == '__main__':
    main()
