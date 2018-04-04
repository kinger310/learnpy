import re
import reprlib

RE_WORDS = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORDS.findall(text)

    # def __getitem__(self, index):
    #     return self.words[index]
    #
    # def __len__(self):
    #     return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word

