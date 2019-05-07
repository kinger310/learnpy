import heapq
from PIL import Image
import numpy as np

img = Image.open("matrix_raw.jpg").convert('L')
img_ndarray = np.asarray(img, dtype='float64')  # 将图像转化为数组并将像素转化到0-1之间
lam, P = np.linalg.eig(img_ndarray)
# lam = np.real(lam)
k_largest = heapq.nlargest(100, lam)
# lam.sort()
# lam[50:] = [0]*(lam.shape[0] - 50)
new_lam = []
for i in lam:
    if i in k_largest:
        new_lam.append(i)
    else:
        new_lam.append(0)

LAM = np.diag(new_lam)
data = np.round(np.real(P.dot(LAM).dot(np.linalg.inv(P))))


new_im = Image.fromarray(data)
new_im.show()
print("ok")