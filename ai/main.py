import numpy as np
from defs import *

weights = np.load('weights.npy')

mxm = .9 # <= 1
m = 0
i = 0
while m < mxm:
    code = []
    for e in range(4): code.append(random.randint(0, 1))
    for e in range(4, 9): code.append(random.randint(0, 9))
    m = softmax(np.dot(np.array(code), weights))[1]
    i += 1
print(m, i)
get_img(code)[0].show()
