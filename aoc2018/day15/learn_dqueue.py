import collections


def breadth_first_search(graph, root):
    visited, queue = set(), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: []}
    print(breadth_first_search(graph, 0))
