from numpy import loadtxt, zeros, mean
from pylab import plot, show
data = loadtxt("millikan.txt", float)
x = data[:, 0]
y = data[:, 1]
E_x = sum(x)/len(x)
E_y = sum(y)/len(y)
E_xx= sum(x * x)/len(x)
E_xy= sum(x * y)/len(y)
m = (E_xy - E_x * E_y) / (E_xx - E_x * E_x)
c = (E_xx * E_y - E_x * E_xy) / (E_xx - E_x * E_x)

z = m*x + c

plot(x, y, "ko")
plot(x, z)
show()

## get Planck's constant
def photoelectric(freq, voltage):
    V = voltage
    Phi = 8.171104858346687e-19
    e_charge = 1.602e-19
    planck_constant_h = (e_charge * (V + Phi)) / freq
    planck_constant_h = mean(planck_constant_h)
    return planck_constant_h

planck = photoelectric(x, y)
print("We have {}".format(planck))

