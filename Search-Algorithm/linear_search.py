def linear_search(item, array):
    loc = 0
    found = False
    while loc < len(array) and not found:
        if array[loc] == item:
            found = True
        else:
            loc += 1
    return found

