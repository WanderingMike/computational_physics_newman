import IntegrationMethods as IM
import numpy as np
from pylab import plot, show, imshow

#################################
### Part A
#################################

def J(m, r):
    Integration = IM.SimpsonsRuleIntegration("cos({0}*theta - {1}*sin(theta))".format(m, r), ["theta"], 0, np.pi)
    value = Integration.perform_integral_without_error_one_var(1000)
    return (1/np.pi) * value

def part_a():
    x_list = np.linspace(0, 20, 100)
    for i in range(3):
        J_values = np.zeros_like(x_list)
        index = 0
        for x in x_list:
            J_values[index] = J(i, x)
            index += 1

        plot(x_list, J_values, "k")

    show()

#################################
### Part B
#################################


def part_b():
    wave_size = 500 * 10e-9
    k = 2 * np.pi / wave_size
    grid_size = 100
    side=2e-6
    x_event = side/2
    y_event = side/2
    density_matrix = np.zeros([grid_size, grid_size], float)
    spacing = side / grid_size
    for x in range(grid_size):
        i = spacing*x
        for y in range(grid_size):
            j = spacing*y
            intermed = k * np.sqrt((i - x_event)**2 + (j - y_event)**2)
            if intermed == 0:
                density_matrix[x, y] = 0.5
            else:
                density_matrix[x, y] = J(1, intermed) / intermed
        print("x value", x)
    imshow(density_matrix)
    show()

part_a()


