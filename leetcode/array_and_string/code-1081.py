# 1081. Smallest Subsequence of Distinct Characters
# Return the lexicographically smallest subsequence of text 
# that contains all the distinct characters of text exactly once.

# Example 1:

# Input: "cdadabcc"
# Output: "adbc"
# Example 2:

# Input: "abcd"
# Output: "abcd"
# Example 3:

# Input: "ecbacba"
# Output: "eacb"
# Example 4:

# Input: "leetcode"
# Output: "letcod"
 

# Note:

# 1 <= text.length <= 1000
# text consists of lowercase English letters.

def smallestSubsequence(text: str) -> str:
    last = {k: i for i, k in enumerate(text)}
    stack = []
    for j, c in enumerate(text):
        if c in stack:
            continue
        while stack and stack[-1] > c and j < last[stack[-1]]:
            stack.pop()
        stack.append(c)
    return "".join(stack)

print(smallestSubsequence("cdadabcc"))
