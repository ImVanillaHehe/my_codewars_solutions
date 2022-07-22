def factorial(n):
    if n >0:
        res = 1
        for number in range(1, n+1):
            res *= number
        return res
    elif n < 0:
        return None
    elif n == 0:
        return 1
