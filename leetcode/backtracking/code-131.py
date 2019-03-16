

def partition(s):


    def backtrack(result, path, ss):
        if len(ss) == 0:
            result.append(path)
            return
        for i in range(1, len(ss)+1):
            if ispd(ss[:i]):
                backtrack(result, path+[ss[:i]], ss[i:])

    result = []
    backtrack(result, [], s)
    return result

def ispd(s):
    return s == s[::-1]



print(partition("aab"))