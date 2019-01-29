N = 300


def calc_power(x, y, ser):
    tmp = ((x + 10) * y + ser) * (x + 10)
    _, hundred = divmod(tmp // 100, 10)
    return hundred - 5


dct = {}
for x in range(1, N + 1):
    for y in range(1, N + 1):
        dct[(x, y)] = calc_power(x, y, 4455)

# sum_ = float("-inf")
res_dct = {}
res_size_dct = {}
for x in range(1, N + 1):
    for y in range(1, N + 1):
        res_size_dct = {}
        pre_sum = 0
        for size in range(1, N + 2 - max(x, y)):
            for x_ in range(x, x + size):
                pre_sum += dct[(x_, y + size - 1)]
            for y_ in range(y, y + size):
                pre_sum += dct[(x + size - 1, y_)]
            pre_sum -= dct[(x_, y_)]
            res_size_dct[(x, y, size)] = pre_sum
        *_, zz = max(res_size_dct, key=res_size_dct.get)
        res_dct[(x, y, zz)] = res_size_dct[(x, y, zz)]
        print(x, y, zz, res_dct[(x, y, zz)])

print(max(res_dct, key=res_dct.get))
xxx, yyy, zzz = max(res_dct, key=res_dct.get)
print(xxx, yyy, zzz, res_dct[(xxx, yyy, zzz)])
