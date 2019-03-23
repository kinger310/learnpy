

def decodeString(s: str) -> str:
    stack = []
    stack.append(["", 0])
    num = ""
    for c in s:
        if c.isdigit():
            num += c
        elif c == "[":
            stack.append(["", int(num)])
            num = ""
        elif c == "]":
            st, k = stack.pop()
            stack[-1][0] += st * k
        else:
            stack[-1][0] += c
    return stack[0][0]


print(decodeString("10[a3[b2[c]]]"))
print(decodeString("3[a]2[c]"))
print(decodeString("2[abc]3[cd]ef"))
