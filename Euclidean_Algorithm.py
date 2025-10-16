"""The Euclidean Algorithm is used to find the greatest common divisor (GCD) of any two numbers. 
Takes as input two integers a and b satisfying a >= b >= 0. 
If b = 0, output a, and terminate the algorithm. 
If b != 0, divide a by b to get a = qb + r for some q,r in the integers (Z) with 0 <= r < b, 
and then rerun the algorithm on the new integers b and r.
"""

import numpy as np


def compute_euclidean_algorithm(a, b):
    if b == 0:
        return a
    a = abs(a)
    b = abs(b)
    if a < b:
        a, b = b, a
    q = a // b
    r = a - q * b
    return compute_euclidean_algorithm(b, r)


def main():
    compute_euclidean_algorithm(1073, -1537)


if __name__ == '__main__':
    main()
