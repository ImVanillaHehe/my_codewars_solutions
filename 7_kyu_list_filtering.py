def filter_list(list):
    new_list = []
    for item in list:
        if type(item) == int:
            new_list.append(item)
    return new_list

