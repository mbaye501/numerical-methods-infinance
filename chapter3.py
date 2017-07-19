from math import *
import numpy as np


# takes a integer number and return the binary representation
def dec_to_binary(n):
    n0 = n
    b = ""
    while (n0 > 0):
        Q = floor(n0 / 2)
        b += str(n0 - 2 * Q)
        n0 = Q
    print(b[::-1])

# example 3.2 illustrating the impact of bad conditioning
def bad_conditioning_example():
    polynomial_1 = [1, -36, 546, -4536, 22449, -67284, 118124, -109584, 40320]
    polynomial_2 = [1, -36.001, 546, -4536, 22449, -67284, 118124, -109584, 40320]
    print ("polinomial 1 roots are:\n ", np.roots(polynomial_1))
    print("polinomial 2 roots are:\n ", np.roots(polynomial_2))



dec_to_binary(13)
bad_conditioning_example()