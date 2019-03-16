def foo(strs):
    flag = strs[0]

    for s in strs[1:]:
        if not s or flag[0] != s[0]:
            return ""
        tmp = ""
        for x, y in zip(s, flag):
            if x == y:
                tmp += x
            else:
                break
        flag = tmp
    return flag


def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)


def bar(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, ch in enumerate(shortest):
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest


strs = ["flower", "flow", "flight"]
# strs = ["abower", "fer", "flighter"]
print(foo(strs))
print(longestCommonPrefix(strs))
print(bar(strs))