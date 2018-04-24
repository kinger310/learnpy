# -*- coding: utf-8 -*-
import random
import pickle

from PIL import Image, ImageChops
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def convert_img2array(im):
    xoff = random.randint(-3, 3)
    ima = ImageChops.offset(im, xoff, 0)
    a = np.array(ima).reshape(-1)
    return a


def main():
    # train image data
    images = [Image.open(r"C:\PycharmProjects\ppdai3\learn_vc\train_data\mumu_{}_L.png".format(i)) for i in range(10)]
    datas = np.array([convert_img2array(im) for im in images for _ in range(100)]) / 255
    labels = np.array([i for i in range(10) for _ in range(100)])
    print(datas.shape)
    print(labels.shape)

    X_train, X_test, y_train, y_test = train_test_split(datas, labels, test_size=0.33, random_state=42)
    model = MLPClassifier(hidden_layer_sizes=(10, 10), learning_rate_init=0.0001, verbose=True, max_iter=5000, tol=-10)
    model.fit(X_train, y_train)
    print(model.score(X_test, y_test))
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

if __name__ == '__main__':
    main()

