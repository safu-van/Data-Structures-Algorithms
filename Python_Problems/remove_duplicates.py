# Remove duplicates from List/Array.


# Using set()
def remove_dup(lst):
    result = list(set(lst))
    return result

print(remove_dup([1,2,3,2,4,3,2]))


# Using Loop
def remove_dupp(lst):
    i = 0
    length = len(lst)
    nums = set()

    while i < length:
        if lst[i] in nums:
            lst.pop(i)
            length -= 1
            i -= 1
        nums.add(lst[i])
        i += 1

    return  lst

print(remove_dupp([1,2,3,2,4,3,2,5,5]))