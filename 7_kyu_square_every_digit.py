def square_digits(num):
    new_n = ''.join(str(int(i)**2) for i in str(num))
    return int(new_n)
