def likes(names):
    x = len(names)
    if x >= 4:
        return f'{names[0]}, {names[1]} and {x - 2} others like this'
    elif x == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif x == 2:
        return f'{names[0]} and {names[1]} like this'
    elif x == 1:
        return f'{names[0]} likes this'
    elif x == 0:
        return f'no one likes this'