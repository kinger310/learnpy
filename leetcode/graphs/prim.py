import collections
import heapq


def mst(input):
    adj_lst = collections.defaultdict(list)
    for i, j, w in input:
        adj_lst[i].append((w, i, j))
        adj_lst[j].append((w, j, i))

    vertex = list(adj_lst.keys())
    start = vertex[0]
    used = set(start)
    usable_edges = adj_lst[start]
    heapq.heapify(usable_edges)

    mst = 0
    result = []
    while usable_edges:
        cost, n1, n2 = heapq.heappop(usable_edges)
        if n2 not in used:
            used.add(n2)
            result.append((n1, n2))
            mst += cost
            for e in adj_lst[n2]:
                if e[2] not in used:  # 避圈
                    heapq.heappush(usable_edges, e)
    return mst, result


input_lst = []
with open("input.txt") as file:
    for line in file:
        a, b, w = line.strip().split(" ")
        input_lst.append([a, b, int(w)])

print(mst(input_lst))

print("ok")
