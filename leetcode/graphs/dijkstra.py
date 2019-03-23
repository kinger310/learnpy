import collections

def shortest_path(input, start, end):
    graph = {(i, j): w for i, j, w in input}
    adj_lst = collections.defaultdict(list)
    for i,j,_ in input:
        adj_lst[i].append(j)
    vertex = list(adj_lst.keys())

    return 0


input = [
    [0,1,10],
    [0,2,5],
    [1,2,2],
    [1,4,1],
    [2,1,3],
    [2,3,2],
    [2,4,9],
    [3,0,7],
    [3,4,6],
    [4,3,6]
]

# shortest_path(input, 0, 3)  #  output 7
shortest_path(input, 0, 4)  #  output 9