
class UF:
    def __init__(self, n):
        self.par = {i: i for i in n}
        self.count = {i: 1 for i in n}

    def root(self, i):
        while i != self.par[i]:
            self.par[i] = self.par[self.par[i]]
            i = self.par[i]
        return i

    def connected(self, i, j):
        return self.root(i) == self.root(j)

    # union by size
    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        new_count = self.count[i] + self.count[j]
        if self.count[i] <= self.count[j]:
            self.par[i] = j
            self.count[j] = new_count
        else:
            self.par[j] = i
            self.count[i] = new_count

    # returns the maxium size of union
    def maxUnion(self):
        return max(self.count)


def mst(input):
    graph = {(i, j): w for i, j, w in input}
    graph.update({(j, i): w for i, j, w in input})
    vertex = set()
    for i, _ in graph:
        vertex.add(i)
    uf = UF(vertex)
    sorted_edges = sorted(input, key=lambda x: x[2])
    A = []
    minimum_sum_weight = 0
    for u, v, weight in sorted_edges:
        if len(A) == len(vertex) - 1:
            break
        if not uf.connected(u, v):
            A.append((u, v))
            minimum_sum_weight+= weight
            uf.union(u, v)
    return minimum_sum_weight, A


input_lst = []
with open("input.txt") as file:
    for line in file:
        a, b, w = line.strip().split(" ")
        input_lst.append([a, b, int(w)])

print(mst(input_lst))

print("ok")
