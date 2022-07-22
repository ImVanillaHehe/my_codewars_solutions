def last(s):
    list1 = list(s.split())
    list1.sort(key=lambda x: str(x)[-1])
    return list1
