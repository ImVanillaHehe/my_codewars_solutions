def sort_array(number):
    odds = sorted((i for i in number if i % 2 != 0), reverse = True)
    return [i if i %2 == 0 else odds.pop() for i in number]
