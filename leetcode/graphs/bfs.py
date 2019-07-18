from collections import defaultdict, deque

graph = defaultdict(set, {1: {(2, 2), (5, 2)}, 2: {(3, 3)}, 3: {(4, 4)}, 5: {(6, 3), (7, 3)}, 6: {(9, 4)}, 7: {(8, 4)}})
suborgs = {key: [] for key, _ in graph[1]}
for suborg in suborgs:
    queue = deque(graph[suborg])
    while queue:
        node, orgtype = queue.popleft()
        if orgtype != 4:
            queue.extend(graph[node])
        else:
            suborgs[suborg].append(node)
print(suborgs)
