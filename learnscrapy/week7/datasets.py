from sklearn.datasets import make_moons
import matplotlib.pyplot as plt
plt.style.use('ggplot')

X, y = make_moons(
    n_samples=500,
    random_state=1,
    noise=0.3
)
plt.plot(X[y == 0, 0], X[y == 0, 1], 'b.')
plt.plot(X[y == 1, 0], X[y == 1, 1], 'r+')
plt.show()




