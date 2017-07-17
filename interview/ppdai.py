def foo1(string):
    count = 0
    new_str = string[0]
    for i, c in enumerate(string[:-1]):
        if c == string[i+1]:
            count += 1
        else:
            new_str += string[i+1]
    return new_str, count


def foo(string):
    my_list = list(string)
    count = 0
    new_str = my_list[0]
    for i in range(len(my_list)-1):
        if my_list[i] == my_list[i+1]:
            count += 1
        else:
            new_str += my_list[i+1]
    return new_str, count

my_str = "aaaaabba"
print(foo1(my_str))

from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.columns = df.columns.str[:-5].str.replace(' ', '_')
df['target'] = pd.DataFrame(iris.target)

# for i, row in df.iterrows():
#     print(i, row)
for tup in df.itertuples():
    print(tup.sepal_length)

N = 100000
df1 = pd.DataFrame({'a': np.random.randn(N), 'b': np.random.randn(N)})
# %timeit
y = [x.a for x in df1.itertuples()]  # Wall time: 343 ms

# %time
y = [x.a for i, x in df1.iterrows()]  # Wall time: 18 s


import PyPDF2
path = r'C:\Users\Wangdi\Desktop\《走向共和》剧本.pdf'

nums = []
count=100000
import time
t = time.clock()
for i in range(count):
    nums.append(i)
nums.reverse()
print(time.clock()-t)
nums = []
t = time.clock()
for i in range(count):
    nums.insert(0, i)

print(time.clock()-t)

import pandas as pd

df = pd.read_clipboard()






