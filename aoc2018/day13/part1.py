
class Cart:
    def __init__(self, t, node):
        self.t = t
        self.node = node
        self.cnt = 0  # intersection count
        self.crash = False


vmap = {
    1: "/", 2: "\\", 3: "+", 4: "-", 5: "|"
}

move_map = {
    ">": {
        "next": (1, 0),
        "/": "^",
        "-": ">",
        "\\": "v",
        "left": "^",
        "straight": ">",
        "right": "v",
    },
    "<": {
        "next": (-1, 0),
        "/": "v",
        "-": "<",
        "\\": "^",
        "left": "v",
        "straight": "<",
        "right": "^",
    },
    "v": {
        "next": (0, 1),
        "\\": ">",
        "|": "v",
        "/": "<",
        "left": ">",
        "straight": "v",
        "right": "<",
    },
    "^": {
        "next": (0, -1),
        "\\": "<",
        "|": "^",
        "/": ">",
        "left": "<",
        "straight": "^",
        "right": ">",
    },
}


class Solution:
    def __init__(self):
        self.graph, self.tp, self.ct, self.height, self.width = self.make_graph()

    # corner 1, straight 0; intersection 2

    def make_graph(self):
        graph = {}
        tp = {}
        ct = []
        with open("input") as f:
            j = 0
            width = 0
            for line in f.readlines():
                width = len(line.strip("\n"))
                for i, s in enumerate(line.strip("\n")):
                    graph[(i, j)] = s
                    if s == " ":
                        pass
                    elif s == "/":
                        tp[(i, j)] = 1
                    elif s == "\\":
                        tp[(i, j)] = 2
                    elif s == "+":
                        tp[(i, j)] = 3
                    elif s == "-":
                        tp[(i, j)] = 4
                    elif s == "|":
                        tp[(i, j)] = 5
                    elif s in ["<", ">"]:
                        tp[(i, j)] = 4
                        ct.append(Cart(s, (i, j)))
                    elif s in ["v", "^"]:
                        tp[(i, j)] = 5
                        ct.append(Cart(s, (i, j)))
                j += 1
        return graph, tp, ct, j, width

    def print_graph(self, ticks):
        if 215 < ticks < 220:
            with open(f"output{ticks}", "w") as file:
                for j in range(self.height):
                    for i in range(self.width):
                        file.write(self.graph[(i, j)])
                    file.write("\n")

    def solve(self):
        ticks = 0
        while True:
            # print(ticks)
            # self.print_graph(ticks)
            # ct 中，小车要排序，左上者先行，右下者后行
            self.ct = sorted(self.ct, key=lambda x: x.node)
            remain = self.move()
            if len(remain) == 1:
                print("remain", remain[0].node)
                break
            ticks += 1
            if ticks > 22000:
                break

    def move(self):
        for cart in self.ct:
            if cart.crash:
                # 小车毁掉了就不再
                continue
            self.graph[cart.node] = vmap[self.tp[cart.node]]
            cart.node = tuple(x + y for x, y in zip(cart.node, move_map[cart.t]["next"]))
            tag = self.graph[cart.node]

            if tag in move_map:
                print(cart.node)
                # 消灭俩小车,重置俩小车的图标识
                # ## 但是消灭了以后，for cart in self.ct 另一辆小车还是会迭代！所以给cart设置crash属性是个不错的方法
                self.graph[cart.node] = vmap[self.tp[cart.node]]
                for c in self.ct:
                    if c.node == cart.node:
                        c.crash = True
                continue
            if tag == "+":
                if cart.cnt % 3 == 0:
                    self.graph[cart.node] = move_map[cart.t]["left"]
                elif cart.cnt % 3 == 1:
                    self.graph[cart.node] = move_map[cart.t]["straight"]
                else:
                    self.graph[cart.node] = move_map[cart.t]["right"]
                cart.cnt += 1
            else:
                self.graph[cart.node] = move_map[cart.t][tag]

            cart.t = self.graph[cart.node]

        remain = [c for c in self.ct if not c.crash]
        return remain


if __name__ == '__main__':
    import time
    start = time.time()
    s = Solution()
    print(s.solve())
    print(time.time()-start)
