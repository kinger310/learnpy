# -*- coding: utf-8 -*-

'''
from sklearn.neighbors import NearestNeighbors
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
plt.scatter(X[:, 0], X[:, 1])
estimator = NearestNeighbors(n_neighbors=3, algorithm='ball_tree')
estimator.fit(X)
distances, indices = estimator.kneighbors(X)
distances
indices
'''



# import csv

# with open(r'./learnaffinity/iris.data', 'r') as file:
#     # lines = csv.reader(csvfile)
#     for row in file:
#         print(str(row).strip())
# -*- Handle data -*-
import random
import csv


def load_dataset(filename, split, training_set=[], test_set=[]):
    with open(filename, 'r') as file:
        lines = csv.reader(file)
        data = list(lines)
        for x in range(len(data)-1):
            for y in range(4):
                data[x][y] = float(data[x][y])
            if random.random() < split:
                training_set.append(data[x])
            else:
                test_set.append(data[x])
'''
trainingSet = []
testSet = []
load_dataset(r'D:\ProgramFiles\PycharmProjects\learnpy\learnaffinity\iris.data', 0.66, trainingSet, testSet)
print('Train: ' + repr(len(trainingSet)))
print('Test: ' + repr(len(testSet)))
'''

# 2. Similarity
import math
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)
'''
data1 = [2, 2, 2, 'a']
data2 = [4, 4, 4, 'b']
distance = euclideanDistance(data1, data2, len(data1)-1)
print('Distance: ' + repr(distance))
'''
# 3. Neighbors
def getNeighbors(training_set, test_instance, k):
    distances = []
    length = len(test_instance) - 1
    for i in range(len(training_set)):
        distance = euclideanDistance(test_instance, training_set[i], length)
        distances.append((training_set[i], distance))
    distances.sort(key=lambda x: x[1])
    neighbors = []
    for j in range(k):
        neighbors.append(distances[j][0])
    return neighbors
'''
train_set = [[2, 2, 2, 'a'], [4, 4, 4, 'b'], [4, 6, 5, 'c']]
test_instance = [5, 5, 5, 'd']
k = 2
neighbors = getNeighbors(train_set, test_instance, k)
print(neighbors)
'''
# 4. Response  the next task is to devise a predicted response based on those neighbors.

def getResponse(neighbors):
    class_votes = {}
    for i in range(len(neighbors)):
        response = neighbors[i][-1]
        if response in class_votes:
            class_votes[response] += 1
        else:
            class_votes[response] = 1
    sorted_votes = sorted(class_votes.items(), key=lambda x: x[1], reverse=True)
    return sorted_votes[0][0]
'''
neighbors = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
response = getResponse(neighbors)
print(response)
'''
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return correct / float(len(testSet)) * 100.0
'''
testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
predictions = ['a', 'a', 'a']
accuracy = getAccuracy(testSet, predictions)
print(accuracy)
'''
def main():
    training_set = []
    test_set = []
    split = 0.67
    load_dataset(r'D:\ProgramFiles\PycharmProjects\learnpy\learnaffinity\iris.data', split, training_set, test_set)
    print('Train set:' + repr(len(training_set)))
    print('Test: ' + repr(len(test_set)))
    predictions = []
    k = 3
    for x in range(len(test_set)):
        neighbors = getNeighbors(training_set, test_set[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(test_set[x][-1]))
    accuracy = getAccuracy(test_set, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

if __name__ == '__main__':
    main()


