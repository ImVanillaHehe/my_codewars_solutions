from math import sqrt

def is_square(n):
    if n >= 0:
        if sqrt(n) % 1 == 0:
            return True
    return False
