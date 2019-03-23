def longestValidParentheses(s):
    dp, stack = [0] * (len(s) + 1), []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                p = stack.pop()
                dp[i + 1] = dp[p] + i - p + 1
    return max(dp)  # TMD太灵活了



def longestValidParentheses2(s: 'str') -> 'int':
    stack = [-1]
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# print(longestValidParentheses(")()())"))
# print(longestValidParentheses("((())(()"))
# print(longestValidParentheses2("((()"))
# print(longestValidParentheses2("()(()"))
print(longestValidParentheses2("()))(())"))
print(longestValidParentheses2("((()))("))
print(longestValidParentheses2("((()))()"))

import heapq
l = [6,1,2,3,4,5]
heapq.heapify(l)

