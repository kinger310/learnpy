# calculate the m*n X= [x_1, ..., x_n]
# D_ij = ||x_i - x_j||^2
#

import numpy as np
import numpy.linalg as la
import time

X = np.array([range(0, 500), range(500, 1000)])
m, n = X.shape

t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        D[i, j] = la.norm(X[:, i] - X[:, j]) ** 2
        D[j, i] = D[i, j]
print(time.time() - t)

t = time.time()
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        d = X[:, i] - X[:, j]
        D[i, j] = np.dot(d, d)
        D[j, i] = D[i, j]
print(time.time() - t)

t = time.time()
G = np.dot(X.T, X)
D = np.zeros([n, n])
for i in range(n):
    for j in range(i + 1, n):
        D[i, j] = G[i, i] - G[i, j] * 2 + G[j, j]
        D[j, i] = D[i, j]
print(time.time() - t)

t = time.time()
G = np.dot(X.T, X)
H = np.tile(np.diag(G), (n, 1))
D = H + H.T - G * 2
print(time.time() - t)
