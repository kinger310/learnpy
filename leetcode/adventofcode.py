import string

# len_l = []
# import string
# for c, C in zip(string.ascii_lowercase, string.ascii_uppercase):
#     l = []
#     for x in s:
#         if x == c or x == C:
#             continue
#         if not l or abs(ord(x) - ord(l[-1])) != 32:
#             l.append(x)
#         else:
#             l.pop()
#     len_l.append(len(l))
#     print(len(l))
# print(len_l)
# print(min(len_l))

from collections import Counter
from itertools import combinations
from collections import defaultdict

import string


def foo(stri):
    dur = {K: 61 + i for i, K in enumerate(string.ascii_uppercase)}

    string_lst = stri.split("\n")
    graph = defaultdict(list)
    available = defaultdict(list)
    for s in string_lst:
        graph[s[5]].append(s[-12])
        available[s[-12]].append(s[5])
    start = sorted(list(set(graph) - set(available)))
    result = []
    # for p in start:
    #     for next in graph[p]:
    #         available[next].remove(p)
    #     result.append(p)
    # w1 :A, w2: E, w3 : M, w4: P, w5: None
    sd = max([v for k, v in dur.items() if k in start])
    while available:
        # sd += max([v for k, v in dur.items() if k in start])
        # key which is none
        for p in start:
            for next in graph[p]:
                available[next].remove(p)
            if p in available:
                available.pop(p)
            result.append(p)
        start = sorted([key for key in available if not available[key]])


    return "".join(result), sd
# AEMPNOJWIZCDFSUKXBQTHVLGRY

stri = """Step A must be finished before step N can begin.
Step P must be finished before step R can begin.
Step O must be finished before step T can begin.
Step J must be finished before step U can begin.
Step M must be finished before step X can begin.
Step E must be finished before step X can begin.
Step N must be finished before step T can begin.
Step W must be finished before step G can begin.
Step Z must be finished before step D can begin.
Step F must be finished before step Q can begin.
Step U must be finished before step L can begin.
Step I must be finished before step X can begin.
Step X must be finished before step Y can begin.
Step D must be finished before step Y can begin.
Step S must be finished before step K can begin.
Step C must be finished before step G can begin.
Step K must be finished before step V can begin.
Step B must be finished before step R can begin.
Step Q must be finished before step L can begin.
Step T must be finished before step H can begin.
Step H must be finished before step G can begin.
Step V must be finished before step L can begin.
Step L must be finished before step R can begin.
Step G must be finished before step Y can begin.
Step R must be finished before step Y can begin.
Step G must be finished before step R can begin.
Step X must be finished before step V can begin.
Step V must be finished before step Y can begin.
Step Z must be finished before step U can begin.
Step U must be finished before step R can begin.
Step J must be finished before step Y can begin.
Step Z must be finished before step C can begin.
Step O must be finished before step L can begin.
Step C must be finished before step H can begin.
Step V must be finished before step G can begin.
Step F must be finished before step K can begin.
Step Q must be finished before step G can begin.
Step S must be finished before step Q can begin.
Step M must be finished before step G can begin.
Step T must be finished before step L can begin.
Step C must be finished before step Q can begin.
Step T must be finished before step V can begin.
Step W must be finished before step Z can begin.
Step C must be finished before step K can begin.
Step I must be finished before step C can begin.
Step X must be finished before step Q can begin.
Step F must be finished before step X can begin.
Step J must be finished before step S can begin.
Step I must be finished before step K can begin.
Step U must be finished before step Q can begin.
Step I must be finished before step Q can begin.
Step N must be finished before step H can begin.
Step A must be finished before step T can begin.
Step T must be finished before step G can begin.
Step D must be finished before step T can begin.
Step A must be finished before step X can begin.
Step D must be finished before step G can begin.
Step C must be finished before step T can begin.
Step W must be finished before step Q can begin.
Step W must be finished before step K can begin.
Step V must be finished before step R can begin.
Step H must be finished before step R can begin.
Step F must be finished before step H can begin.
Step F must be finished before step V can begin.
Step U must be finished before step T can begin.
Step K must be finished before step H can begin.
Step B must be finished before step T can begin.
Step H must be finished before step Y can begin.
Step J must be finished before step Z can begin.
Step B must be finished before step Y can begin.
Step I must be finished before step V can begin.
Step W must be finished before step V can begin.
Step Q must be finished before step R can begin.
Step I must be finished before step S can begin.
Step E must be finished before step H can begin.
Step J must be finished before step B can begin.
Step S must be finished before step G can begin.
Step E must be finished before step S can begin.
Step N must be finished before step I can begin.
Step Z must be finished before step F can begin.
Step E must be finished before step I can begin.
Step S must be finished before step B can begin.
Step D must be finished before step L can begin.
Step Q must be finished before step T can begin.
Step Q must be finished before step H can begin.
Step K must be finished before step Y can begin.
Step M must be finished before step U can begin.
Step U must be finished before step K can begin.
Step W must be finished before step I can begin.
Step J must be finished before step W can begin.
Step K must be finished before step T can begin.
Step P must be finished before step Y can begin.
Step L must be finished before step G can begin.
Step K must be finished before step B can begin.
Step I must be finished before step Y can begin.
Step U must be finished before step B can begin.
Step P must be finished before step O can begin.
Step O must be finished before step W can begin.
Step O must be finished before step J can begin.
Step A must be finished before step J can begin.
Step F must be finished before step G can begin."""
y = foo(stri)
print(y)

