

def f(x):
    print(x, x-1)
    return x * (x-1)

def deriv(func, x, delta):
    print(func(x + delta), func(x))
    return (func(x + delta) - func(x)) / delta

print("Actual value is 1")
print("Value at x=1 :", deriv(f, 1, 10e-2))
print("Value at x=1 :", deriv(f, 1, 10e-4))
print("Value at x=1 :", deriv(f, 1, 10e-6))
print("Value at x=1 :", deriv(f, 1, 10e-8))
print("Value at x=1 :", deriv(f, 1, 10e-10))
print("Value at x=1 :", deriv(f, 1, 10e-12))
print("Value at x=1 :", deriv(f, 1, 10e-14))