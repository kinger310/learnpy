# from collections import defaultdict
# graph = defaultdict(list)

graph = {}

with open("input") as file:
    for line in file:
        n = line.strip().split(")")
        graph[n[1]] = n[0]

X = "YOU"
Y = "SAN"
num1= []
num2 = []
while X in graph or Y in graph:
    if X in graph:
        X = graph[X]
        num1.append(X)
    if Y in graph:
        Y = graph[Y]
        num2.append(Y)
    if X in num2:
        print(len(num1)+len(num2[:num2.index(X)]) - 1)
        break
    if Y in num1:
        print(len(num2)+len(num1[:num1.index(Y)]) - 1)
        break

# print(num1)
# print(num2)

