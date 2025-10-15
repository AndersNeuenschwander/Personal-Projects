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
