# %%
# level 0
print(1 << 38)

# %%
# level 1
# https://stackoverflow.com/questions/4406389/if-else-in-a-list-comprehension
import string

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
# def maketrans(s):
#     new_s = "".join([chr(97 + (ord(c) + 2 - 97) % 26) if ord('a') <= ord(c) <= ord('z') else c for c in s])
#     return new_s
s.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])
print(maketrans(s))

# %%
# level 2
import requests
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
html = requests.get(url).text
mess = "".join(re.findall(r"-->(.*)-->", html, re.S))
chars = "".join(re.findall(r'[0-9]|[a-z]|[A-Z]', mess))
print(chars)

# %%
# level 3
import requests
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
html = requests.get(url).text
mess = "".join(re.findall(r"<!--(.*)-->", html, re.S))
chars = "".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', mess))
print(chars)

# %%
# level 4
import requests
from bs4 import BeautifulSoup
import re

l = []
nothing = ""
for i in range(400):
    if i == 0:
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        nothing = "".join(re.findall(r'nothing=(\d+)">', str(soup.a)))
    else:
        nothing_pre = nothing
        url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}".format(nothing)
        soup = BeautifulSoup(requests.get(url).text, 'lxml')
        nothing = "".join(re.findall(r'nothing is (\d+).*', str(soup.body)))
    print(str(i) + nothing)
    if nothing == "":
        nothing = str(int(nothing_pre)/2)
        print(soup.prettify())
    l.append(nothing)
