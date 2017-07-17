# -*- coding: utf-8 -*-
import re


s = 'postcode 200030 200040 010020 476400'
pattern = r'[1-9]\d{5}'
search_result = re.search(pattern, s)
if search_result:
    print(search_result.group())

find_result = re.findall(pattern, s)
print(find_result)

match_result = re.match(pattern, s)
if match_result:
    print(match_result.group(0))
s1 = '200030 postcode 200040 010020 476400'
match_result = re.match(pattern, s1)
if match_result:
    print(match_result.group(0))

m = re.search(r'PY.*N', 'PYANBNCNDN')
m.group()
m = re.search(r'PY.*?N', 'PYANBNCNDN')
m.group()

# Baby name




