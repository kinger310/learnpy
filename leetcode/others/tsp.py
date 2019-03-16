MAX = 1000000
distances = {(0,1):1,(0,2):5,(0,3):6, (1,2):4,(1,3):2, (2,3):3, (0,0):MAX, (1,1):MAX,(2,2):MAX,(3,3):MAX}

n =  4

def foo(n):
    visit = [False]* n

    def search(idx, count, min_val):
        if count == n:
            return 0
        t = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                t = distances[tuple(sorted((idx, i)))] + search(i, count+1, min_val)
                visit[i] = False
        if t < min_val[0]:
            min_val[0] = t

        return min_val[0]

    min_val = [float("inf")]
    return search(0, 0, min_val)

print(foo(n))

# import tsp
# t = tsp.tsp([(0,0), (0,1), (1,0), (1,1)])
# print(t)  # distance, node index list
# # >>>
# # (4, [0, 1, 3, 2])
#
# mat = [[0, 1, 5, 6],
#        [1, 0, 4, 2],
#        [5, 4, 0, 3],
#        [6, 2, 3, 0]]  # Distance Matrix
# r = range(len(mat))
# # Dictionary of distance
# dist = {(i, j): mat[i][j] for i in r for j in r}
# print(tsp.tsp(r, dist))
# # >>>
# # (4, [0, 1, 3, 2])