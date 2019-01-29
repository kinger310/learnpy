from collections import deque


def recursive_dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    extend_pre = set(graph[start]) - set(visited)
    for node in extend_pre:
        if node not in visited:
            recursive_dfs(graph, node, visited)
    return visited


def iterative_dfs(graph, start):
    """iterative depth first search from start"""
    visited = []
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            extend_pre = set(graph[vertex]) - set(visited)
            stack.extend(extend_pre)
    return visited


def iterative_bfs(graph, start):
    """iterative breadth first search from start"""
    visited = []
    stack = deque([start])
    while stack:
        vertex = stack.popleft()
        if vertex not in visited:
            visited.append(vertex)
            extend_pre = set(graph[vertex]) - set(visited)
            stack.extend(extend_pre)
    return visited


"""
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
"""

graph = {'A': ['B', 'C'], 'B': ['D', 'E'],
         'C': ['D', 'E'], 'D': ['E'], 'E': ['A']}
print('recursive dfs ', recursive_dfs(graph, 'A'))
print('iterative dfs ', iterative_dfs(graph, 'A'))
print('iterative bfs ', iterative_bfs(graph, 'A'))
