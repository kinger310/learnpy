# from collections import defaultdict
# graph = defaultdict(list)

graph = {}

with open("input") as file:
    for line in file:
        n = line.strip().split(")")
        graph[n[1]] = n[0]


total = 0
for x in graph:
    num = 0
    while x in graph:
        num += 1
        x = graph[x]
    total += num
print(total)

