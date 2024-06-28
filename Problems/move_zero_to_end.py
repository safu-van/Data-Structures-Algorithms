# Move any numbers to end of the List/Array


def move_to_end(lst, num):
    i, j = 0, len(lst)-1
    
    while i < j:
        if lst[i] == num:
            if lst[j] != num:
                lst[i], lst[j] = lst[j], lst[i]
            j -= 1
        else:
            i += 1

    return lst

print(move_to_end([2, 1, 2, 4, 2, 3, 2], 2))