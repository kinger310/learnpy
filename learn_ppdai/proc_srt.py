
with open("wd.txt", "r", encoding="utf-8") as file:
    lst = []
    cnt = 0
    dct = {}
    for line in file:
        if cnt % 5 == 0:
            dct["num"] = int(line.strip()) + 1
        elif cnt % 5 == 1:
            dct["track"] = line
        elif cnt % 5 == 2:
            dct["en"] = line
        elif cnt % 5 == 3:
            dct["cn"] = line
        elif cnt % 5 == 4:
            dct["kong"] = line
            lst.append(dct)
            dct = {}
        cnt += 1

with open("new_wd.txt", "w", encoding="utf-8") as f:
    for dct in lst:
        f.write(str(dct["num"]) + "\n")
        f.write(dct["track"])
        f.write(dct["cn"])
        f.write(dct["en"])
        f.write(dct["kong"])


print("ok")


