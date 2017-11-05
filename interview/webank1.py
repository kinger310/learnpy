
# n = raw_input()
n = input()
s_list = []
for i in range(int(n)):
    ss = input()
    s_list.append(ss)
for s in s_list:
    if s != "":
        l = len(s)
        if l >= 10:
            s = s[:1] + str(l - 2) + s[-1:]
        print(s)