from numpy import arange, zeros, append, insert
from pylab import show, scatter


def feigenbaum(num, constantr):
    return constantr * num * (1 - num)


for r in arange(1, 4.01, 0.01):
    x = 0.5
    data = zeros([1000, 2], float)

    for j in range(1000):
        x = feigenbaum(x, r)

    for k in range(1000):
        row = [r, x]
        data[k, :] = row
        x = feigenbaum(x, r)

    scatter(data[:, 0], data[:, 1])

show()
