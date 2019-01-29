from itertools import product


def foo(smap, init_state):
    N = 3
    dct = {"".join(k): "." for k in product("#.", repeat=5)}
    for s in smap.split("\n"):
        kk, vv = s.split(" => ")
        dct[kk] = vv
    pre_state = list("." * N + init_state + "." * 300)

    for j in range(1000):
        # print(j, ": ", "".join(pre_state))
        state = pre_state.copy()
        length = len(pre_state)
        for i in range(length):
            if i < 2:
                status = "." * (2 - i) + "".join(pre_state[:i + 3])
            elif i + 3 > length:
                status = "".join(pre_state[i - 2:]) + "." * (i + 3 - length)
            else:
                status = "".join(pre_state[i - 2:i + 3])
            state[i] = dct[status]
        pre_state = state
        # print(j + 1, ": ", "".join(pre_state))
        # j = 291, sum_291 = 25912; j = 292, sum_292 = 26000; sum_293 = 26088
        # f(x) = 88*x + 304
        res_lst = [idx - N for idx, x in enumerate(pre_state) if x == "#"]
        print(j+1, sum(res_lst))

    return 88*50000000000 + 304


init_state = "####..##.##..##..#..###..#....#.######..###########.#...#.##..####.###.#.###.###..#.####..#.#..##..#"
# init_state = "#..#.#..##......###...###"

smap = """.#.## => .
...## => #
..#.. => .
#.#.. => .
...#. => .
.#... => #
..... => .
#.... => .
#...# => #
###.# => .
..### => #
###.. => .
##.## => .
##.#. => #
..#.# => #
.###. => .
.#.#. => .
.##.. => #
.#### => .
##... => .
##### => .
..##. => .
#.##. => .
.#..# => #
##..# => .
#.#.# => #
#.### => .
....# => .
#..#. => #
#..## => .
####. => #
.##.# => #"""
print(foo(smap, init_state))
