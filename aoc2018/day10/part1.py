import re
import matplotlib.pyplot as plt
from PIL import Image


pat1 = "position=<(.*)> velocity=<(.*)>"

with open("input") as file:
    pos_lst = []
    vec_lst = []
    for line in file.readlines():
        pos, vec = re.findall(pat1, line)[0]
        pos = [int(x) for x in pos.split(",")]
        vec = [int(y) for y in vec.split(",")]
        pos_lst.append(pos)
        vec_lst.append(vec)
        # print(pos, vec)
X = [x[0] for x in pos_lst]
Y = [x[1] for x in pos_lst]
plt.ion()   # 开启interactive mode 成功的关键函数
plt.figure(1)
plt.plot(X, Y, "o")
# plt.show()
ticks = 0
while True:
    plt.clf()

    pos_lst = [(p[0]+v[0], p[1]+v[1]) for p, v in zip(pos_lst, vec_lst)]
    X = [x[0] for x in pos_lst]
    Y = [x[1] for x in pos_lst]

    ticks += 1
    # if ticks % 50 == 0
    # if 10000 < ticks < 10300:
    if ticks == 10136:
        plt.plot(X, Y, "o")
        plt.savefig(f"fig{ticks}.png")
        print(ticks)
        break

minx, maxx = min(X), max(X)
miny, maxy = min(Y), max(Y)

for y in range(miny, maxy+1):
    for x in range(minx, maxx+1):
        if (x, y) in pos_lst:
            print("#", end="")
        else:
            print(".", end="")
    print("\n")


im = Image.open("fig10136.png")

out = im.transpose(Image.FLIP_TOP_BOTTOM)
out.show()