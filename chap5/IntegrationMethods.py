from Equation import Expression
import numpy as np


class SimpsonsRuleIntegration:
    """
    This object takes the integral of a function or a set of data
    using Simpson's Rule integration method. note that Simpson's Rule requires
    an even number of steps to work properly.
    The maximum amount of slices needed to achieve maximum accuracy with sympsons
    rule is 10000. anything more and rounding error is dominant and a waist
    of computation.
    derivation of this method can be found in section 5.1.2 Simpson's Rule
    from 'Computation Physics' by Mark Newman
    """

    def __init__(self, equation, integrating_variables, bounds_a, bounds_b):
        self.equation = equation
        self.bound_a = bounds_a
        self.bound_b = bounds_b
        self.int_var = integrating_variables

    def __f(self, equation, variables):
        f = Expression(equation, variables)
        return f

    def perform_integral_without_error_one_var(self, num_slices):
        int(num_slices)
        f = self.__f(self.equation, self.int_var)
        width = (self.bound_b - self.bound_a) / num_slices
        summation = (f(self.bound_a) + f(self.bound_b))
        summation_even = 0
        summation_odd = 0
        for odd in range(1, num_slices, 2):
            summation_odd += (f(self.bound_a + (odd * width)))
        summation_odd *= 4
        for even in range(2, num_slices, 2):
            summation_even += (f(self.bound_a + (even * width)))
        summation_even *= 2
        summation += summation_odd + summation_even
        summation *= (1 / 3) * width
        return summation