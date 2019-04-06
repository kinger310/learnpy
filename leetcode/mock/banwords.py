import collections
import string
import re



def mostCommonWord(paragraph: str, banned: 'List[str]') -> str:
    w_lst = re.findall(r"\w+", paragraph)
    w_lst = [w.lower() for w in w_lst]
    dct = collections.defaultdict(int)
    for w in w_lst:
        dct[w] += 1
    cnt_lst = sorted([(v, k) for k, v in dct.items()], reverse=True)
    for cnt, w in cnt_lst:
        if w not in banned:
            return w
    return ""


print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))



