import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # def __iter__(self):
    #     for match in RE_WORD.finditer(self.text):
    #         yield match.group()

    # 生成器表达式
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


from itertools import count, takewhile

list(takewhile(lambda x: x < 5, count(1, .5)))

from collections import Iterable
ss = [1, 2, [3, 4, [5]], [6, 7]]

def flat(t):
    for sub in t:
        if isinstance(sub, Iterable):
            yield from flat(sub)
        else:
            yield sub
print(list(flat(ss)))

import itertools
list(itertools.chain.from_iterable(ss))