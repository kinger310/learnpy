# coding=utf8

import re
import pandas as pd

with open("test.txt") as file:
    pre_userid = None
    result = []
    for line in file:
        g1 = re.findall(r"userid=(.*)", line)
        if g1:
            pre_userid = g1[0]
        g2 = re.findall(r"降额至(.*)", line)
        if g2:
            edu = g2[0]
            result.append({"userid": pre_userid, "e_du": edu})
    df = pd.DataFrame(result)
    df.to_csv("res.csv", index=False)





