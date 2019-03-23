def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    if s[0] == "0":
        return 0
    if n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(n-1):
        deco = int(s[i:i + 2])
        if deco == 10 or deco == 20:
            dp[i + 2] = dp[i]
        elif 10 < deco <= 26:
            dp[i + 2] = dp[i + 1] + dp[i]
        elif deco % 10 != 0:
            dp[i + 2] = dp[i + 1]
        else:
            dp[i + 2] = 0
    return dp[-1]

# print(numDecodings("0"))
print(numDecodings("1"))
# print(numDecodings("01")) # expect 0
print(numDecodings("10")) # expect 0
print(numDecodings("20")) # expect 0

print(numDecodings("120")) # expect 1
print(numDecodings("1201")) # expect 1
print(numDecodings("12010")) # expect 1

print(numDecodings("26801"))
print(numDecodings("1221"))
print(numDecodings("1278"))
print(numDecodings("1227"))

print(numDecodings("121212"))