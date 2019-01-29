class Unit:
    def __init__(self, gender, loc, hp):
        self.gender = gender
        self.loc = loc
        self.hp = hp

    def in_range_nodes(self, graph):
        x, y = self.loc
        nodes = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
        return [node for node in nodes if graph[node] == "."]

    def find_enemy(self, graph, units):
        for target in units:
            if self.gender == target.gender:
                continue
            target.in_range_nodes(graph)


class Solution:
    def __init__(self):
        self.graph, self.height, self.width = self.make_graph()
        self.units = self.init_units()

    def make_graph(self):
        with open("inputtest") as f:
            graph = {}
            j = 0
            width = 0
            for line in f.readlines():
                width = len(line.strip("\n"))
                for i, s in enumerate(line.strip("\n")):
                    graph[(i, j)] = s
                j += 1
        return graph, j, width

    def init_units(self):
        units = []
        for loc, v in self.graph.items():
            if v == "G":
                units.append(Unit("G", loc, 200))
            elif v == "E":
                units.append(Unit("E", loc, 200))
        return sorted(self.units, key=lambda x: (x[1], x[0]))

    def solve(self):
        ticks = 0
        while True:
            # if all(G) or all(E):
            #     break
            for unit in self.units:
                if unit.hp < 0:
                    continue

                unit.find_enemy(self.graph, self.units)



if __name__ == '__main__':
    s = Solution()
    s.solve()
    print("ok")
    import string
