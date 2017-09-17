#
# 主程序：用遗传算法求解y=200*exp(-0.05*x).*sin(x)在[-2 2]区间上的最大值
import pandas as pd
import numpy as np
from numpy.random import randint
import matplotlib.pyplot as plt


def target_fun(x):
    y = 200 * np.exp(-0.05 * x) * np.sin(x)
    return y


def cal_fit(row):
    x = int(''.join([str(j) for j in row.loc[:]]), base=2)
    # % 转化为[-2, 2]区间的实数
    xx = bounds_begin + x * (bounds_end - bounds_begin) / (np.power(bounds_end, bit_length) - 1)
    fit_value = target_fun(xx)
    # print(xx, fit_value)
    return fit_value


def fitness_fun(df_pop):
    # 将二进制转换为十进制
    df_pop['fit_value'] = df_pop.apply(cal_fit, axis=1)
    # % 给适应度函数加上一个大小合理的数以便保证种群适应值为正数
    # regulator = abs(min(df_pop['fit_value'])) + 20
    regulator = 250
    df_pop['fitness'] = df_pop['fit_value'].apply(lambda x: x + regulator)
    # % 计算选择概率
    fsum = sum(df_pop['fitness'])
    df_pop['prb_population'] = df_pop['fitness'] / fsum
    df_pop['cumsum'] = df_pop['prb_population'].cumsum(axis=0)
    df_result = df_pop[['fitness', 'cumsum']]
    return df_result


# %子程序：新种群选择操作, 函数名称存储为selection.m
def selection(population, df_fit_and_cumsum):
    # % 从种群中选择两个个体
    cumsump = df_fit_and_cumsum['cumsum']
    seln = []
    for i in range(2):
        r = np.random.rand()
        prand = cumsump - r
        j = 0
        while prand[j] < 0:
            j += 1
        seln.append(j)
    return seln


# %子程序：判断遗传运算是否需要进行交叉或变异, 函数名称存储为IfCroIfMut.m
def if_ctrl_mut(pc):
    N = 100
    test = np.array([0] * N)
    l = round(N * pc)
    test[:l] = 1
    r = randint(0, N)
    pcc = test[r]
    return pcc


def crossover(population, seln, pcrossover):
    pcc = if_ctrl_mut(pcrossover)
    scro = np.zeros((2, bit_length))
    if pcc:
        chb = randint(0, bit_length)
        scro[0, :] = np.r_[population[seln[0], :chb], population[seln[1], chb:]]
        scro[1, :] = np.r_[population[seln[1], :chb], population[seln[0], chb:]]
    else:
        scro[0, :] = population[seln[0], :]
        scro[1, :] = population[seln[1], :]
    return scro


def mutation(snew, pmutation):
    snnew = snew.copy()
    pmm = if_ctrl_mut(pmutation)
    if pmm:
        chb = randint(0, bit_length)
        snnew[chb] = abs(snew[chb] - 1)
    return snnew


bounds = np.array([-2, 2])  # 一维自变量的取值范围
precision = 0.0001  # 运算精度
bounds_begin = bounds[0]
bounds_end = bounds[1]
# 计算如果满足求解精度至少需要多长的染色体
BitLength = np.ceil(np.log2((bounds_end - bounds_begin) / precision))
bit_length = int(BitLength)
pop_size = 50  # 初始种群大小
Generationnmax = 120  # 最大代数
pcrossover = 0.90  # 交配概率
pmutation = 0.09  # 变异概率


def main():
    # %产生初始种群
    population = np.round(np.random.rand(pop_size, bit_length))
    df_population = pd.DataFrame(data=population).applymap(int)

    # %计算适应度,返回适应度Fitvalue和累积概率cumsump
    df_fit_and_cumsum = fitness_fun(df_population)

    scnew = np.zeros_like(population)
    smnew = np.zeros_like(population)
    ymax = []
    ymean = []
    xmax = []
    for gen in range(Generationnmax):
        for j in range(0, pop_size, 2):
            seln = selection(population, df_fit_and_cumsum)  # %选择操作
            scro = crossover(population, seln, pcrossover)  # 交叉操作
            scnew[j, :] = scro[0, :]
            scnew[j+1, :] = scro[1, :]
            smnew[j, :] = mutation(scnew[j, :], pmutation)
            smnew[j+1, :] = mutation(scnew[j+1, :], pmutation)
        population = smnew.copy()
        df_population = pd.DataFrame(data=smnew).applymap(int)
        df_fit_and_cumsum = fitness_fun(df_population)
        fit_value = df_fit_and_cumsum['fitness']
        fmax, nmax = np.max(fit_value), fit_value.idxmax()
        fmean = np.mean(fit_value)
        ymax.append(fmax)
        ymean.append(fmean)
        # % 记录当前代的最佳染色体个体
        x = int(''.join([str(int(j)) for j in population[nmax, :]]), base=2)
        xx = bounds_begin + x * (bounds_end - bounds_begin) / (np.power(bounds_end, bit_length) - 1)
        xmax.append(xx)

    Bestpopulation = xx
    Besttargetfunvalue = target_fun(xx)
    plt.plot(range(Generationnmax), ymax, 'r-*')
    plt.plot(range(Generationnmax), ymean, 'b-.')
    plt.show()
    # % 绘制经过遗传运算后的适应度曲线。一般地，如果进化过程中种群的平均适应度与最大适
    # % 应度在曲线上有相互趋同的形态，表示算法收敛进行得很顺利，没有出现震荡；在这种前
    # % 提下，最大适应度个体连续若干代都没有发生进化表明种群已经成熟。

    print('ok')


if __name__ == '__main__':
    main()
