def strStr(self, haystack: 'str', needle: 'str') -> 'int':

    return 0


# kmp algorithm
# "ABCDABD"
def partial_table(pat):
    table = []
    for i in range(len(pat)):
        p = pat[:i+1]
        length = len(p)
        pre = {p[:i] for i in range(length)}
        post = {p[j:] for j in range(1, length+1)}
        common = max(pre & post)
        table.append(len(common))
    return table

def kmp_match(ms, pat):
    table = partial_table(pat)
    m = len(ms)
    n = len(pat)
    cur = 0
    while cur <= m - n:
        for j in range(n):
            if ms[j+cur] != pat[j]:
                cur += max(j - table[j - 1], 1)
                break
        else:
            return cur
    return -1


# print(partial_table("ABCDABD"))

ms = "abbabaaaabbbaabaabaabbbaaabaaaaaabbbabbaabbabaabbabaaaaababbabbaaaaabbbbaaabbaaabbbbabbbbaaabbaaaaababbaababbabaaabaabbbbbbbaabaabaabbbbababbbababbaaababbbabaabbaaabbbba"
pat = "bbbbbbaa"

# print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
print(kmp_match(ms, pat))

def strStr(haystack, needle):
    if needle == "":
        return 0
    for i in range(len(haystack)-len(needle)+1):
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                break
            if j == len(needle)-1:
                return i
    return -1

strStr("hello", "leod")
