def two(value):
    if value >1000:
        return value
    return two(value*2)


print(two(1))