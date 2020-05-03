import collections


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def overlap(self, a, b):
        return a.start <= b.end and a.end >= b.start

    def build_graph(self, intervals):
        graph = collections.defaultdict(list)
        for i, interval in enumerate(intervals):
            for j in range(i + 1):
                if self.overlap(interval, intervals[j]):
                    graph[interval].append(intervals[j])
                    graph[intervals[j]].append(interval)
        return graph

    def merge_nodes(self, nodes):
        s = min(node.start for node in nodes)
        e = max(node.end for node in nodes)
        return Interval(s=s, e=e)

    def connect_components(self, graph, intervals):
        visited = set()
        component = collections.defaultdict(list)
        comp_number = 0

        def mark_component_dfs(interval):
            stack = [interval]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    component[comp_number].append(node)
                    stack.extend(graph[node])

        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                comp_number += 1

        return component, comp_number

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        graph = self.build_graph(intervals)
        component, comp_number = self.connect_components(graph, intervals)

        return [self.merge_nodes(component[comp]) for comp in range(comp_number)]
