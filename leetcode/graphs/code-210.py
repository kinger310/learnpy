# 210. Course Schedule II
# 有向图的拓扑排序问题
# 设置三种状态：
# 初始状态：0，表示结点未被访问
# 正在被访问状态: -1
# 访问结束状态： 1
#
#
import collections

WHITE = 0
GRAY = -1
BLACK = 1


def findOrder(numCourses: int, prerequisites: 'List[List[int]]') -> 'List[int]':
    # Create the adjacency list representation of the graph
    # graph = [[] for _ in range(numCourses)]
    graph = collections.defaultdict(list)

    for dest, src in prerequisites:
        graph[src].append(dest)

    topological_sorted_order = []
    is_possible = True
    visit = [WHITE] * numCourses

    def dfs(node):
        nonlocal is_possible
        # Don't recurse further if we found a cycle already
        if not is_possible:
            return

        visit[node] = GRAY
        for neighbor in graph[node]:
            if visit[neighbor] == WHITE:
                dfs(neighbor)
            elif visit[neighbor] == GRAY:
                # An edge to a GRAY vertex represents a cycle
                is_possible = False
        # Recursion ends. We mark it as black
        visit[node] = BLACK
        topological_sorted_order.append(node)

    for vertex in range(numCourses):
        if visit[vertex] == WHITE:
            dfs(vertex)
    return topological_sorted_order[::-1] if is_possible else []


print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


# Complexity Analysis
#
# Time Complexity: O(N)
# considering there are NN courses in all.
# We essentially perform a complete depth first search covering all the nodes in the forest.
# It's a forest and not a graph because not all nodes will be connected together.
# There can be disjoint components as well.
# Space Complexity: O(N)
# the space utilized by the recursion stack (not the stack we used to maintain the topologically sorted order)
