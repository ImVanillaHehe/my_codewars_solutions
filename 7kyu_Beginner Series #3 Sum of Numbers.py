def get_sum(a, b):
    arr = []
    if a == b:
        return a
    elif a > b:
        for i in range(b, a + 1):
            arr.append(i)
        return sum(arr)
    else:
        for i in range(a, b+1):
            arr.append(i)
        return sum(arr)



print(get_sum(0,-5))