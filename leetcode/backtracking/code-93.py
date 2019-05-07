# 93. Restore IP Addresses
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# Example:
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]


def restoreIpAddresses(s: str) -> "List[str]":
    def validate(t):
        m = len(t)
        if m == 1:
            return True
        elif m == 2 and 10 <= int(t) <= 99:
            return True
        elif m == 3 and 100 <= int(t) <= 255:
            return True
        else:
            return False

    def backtrack(idx, path):
        if len(path) == 4 and idx < n:
            return
        if len(path) == 4 and idx == n:
            result.append(".".join(path))
            return

        for j in range(1, 4):
            if validate(s[idx:idx + j]):
                backtrack(idx + j, path + [s[idx:idx + j]])

    n = len(s)
    result = []
    backtrack(0, [])
    return result


#  0 的存在

# ip 0-255.0-255.0-255.0-255
# 00010 --> 0.0.0.10
print(restoreIpAddresses("00010"))
print(restoreIpAddresses("000"))
print(restoreIpAddresses("10001010"))
print(restoreIpAddresses("25525511135"))
print(restoreIpAddresses("255255"))
