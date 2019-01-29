
# def run(self, s):
#     split = list(map(int, s.split(" ")))
#     _, r = self.rec(split)
#     return r

def rec(ll):
    nodes = ll[0]
    metadata = ll[1]
    ll = ll[2:]

    if nodes == 0:
        return ll[metadata:], sum(ll[:metadata])

    li = list()
    result = 0
    for n in range(nodes):
        ll, nli = rec(ll)
        li.append(nli)
    for i in range(metadata):
        if ll[i] <= nodes:
            result += li[ll[i] - 1]
    return ll[metadata:], result


s = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
lst = [int(i) for i in s.split(" ")]
# with open("input") as f:
#     for line in f.readlines():
#         lst = [int(i) for i in line.split(" ")]
print(rec(lst))
