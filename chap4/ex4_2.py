from numpy import sqrt

def standard(a, b, c):
    root = sqrt(b**2 - 4 * a * c)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    return x1, x2


def alternative(a, b, c):
    x1 = (2*c) / ( -b - sqrt(b**2 - 4*a*c) )
    x2 = (2*c) / ( -b + sqrt(b**2 - 4*a*c) )
    return x1, x2


def improved_version(a, b, c):
    root = sqrt(b ** 2 - 4 * a * c)
    x1 = (-b + root) / (2 * a)
    x2 = (2 * c) / (-b + sqrt(b ** 2 - 4 * a * c))
    return x1, x2


x1_stand, x2_stand = standard(0.001, 1000, 0.001)
x1_alt, x2_alt = alternative(0.001, 1000, 0.001)
x1_best, x2_best = improved_version(0.001, 1000, 0.001)
print("Standard: ", x1_stand, x2_stand)
print("Alternative: ", x1_alt, x2_alt)
print("Best: ", x1_best, x2_best)



