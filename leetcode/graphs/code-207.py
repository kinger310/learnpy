# 207. Course Schedule
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
#
# Example 1:
#
# Input: 2, [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
# Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    def dfs(v):
        nonlocal is_possible
        if not is_possible:
            return
        visit[v] = -1
        for u in graph[v]:
            if visit[u] == 0:
                dfs(u)
            elif visit[u] == -1:
                is_possible = False
        visit[v] = 1

    graph = [[] for _ in range(numCourses)]
    for src, dest in prerequisites:
        graph[src].append(dest)

    visit = [0] * numCourses
    is_possible = True

    for course in range(numCourses):
        if visit[course] == 0:
            dfs(course)
    return is_possible


# if node v has not been visited, then mark it as 0.
# if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
# if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.

# print(canFinish(3, [[0,2], [1, 2], [0, 1]]))
print(canFinish(4, [[0,1], [1, 2], [2,0],[2,3], [3,0]]))
