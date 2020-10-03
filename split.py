def split_in_two(elements, num):
    if num%2 == 0:
        return elements[2:]
    else:
        return elements[:2]
