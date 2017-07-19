from math import *

# takes a integer number and return the binary representation
def dec_to_binary(n):
    n0 = n
    b = ""
    while(n0>0):
        Q = floor(n0/2)
        b += str(n0-2*Q)
        n0 = Q
    print(b[::-1])


dec_to_binary(3)