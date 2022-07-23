def likes(names):
    more_than_4_names = names[1: -1]
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} likes this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} likes this'
    elif len(names) >=4:
        return f'{names[0]}, {names[1]} and {len(more_than_4_names)} others like this'



