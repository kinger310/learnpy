import collections


def shortest_path(input, start, end):
    graph = {(i, j): w for i, j, w in input}
    adj_lst = collections.defaultdict(list)
    for i, j, _ in input:
        adj_lst[i].append(j)
    vertex = list(adj_lst.keys())
    # init single source
    dist = {}
    prev = {}
    for v in vertex:
        dist[v] = float("inf")
        prev[v] = None
    dist[start] = 0

    u = start
    while u != end:
        u = min(dist, key=dist.get)
        distu = dist[u]
        del dist[u]
        for v in adj_lst[u]:
            if v in dist:
                alter = distu + graph[(u, v)]
                if alter < dist[v]:
                    dist[v] = alter
                    prev[v] = u
    # 输出结果
    stack = [end]
    node = end
    shortest = 0
    while prev[node] is not None:
        stack.append(prev[node])
        shortest += graph[(prev[node], node)]
        node = prev[node]

    return shortest, stack[::-1]


input = [
    [0, 1, 10],
    [0, 2, 5],
    [1, 2, 2],
    [1, 4, 1],
    [2, 1, 3],
    [2, 3, 2],
    [2, 4, 9],
    [3, 0, 7],
    [3, 4, 6],
    [4, 3, 6]
]

print(shortest_path(input, 0, 3))  # output 7
print(shortest_path(input, 0, 4))  # output 9
