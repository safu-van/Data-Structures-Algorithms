# Reverse List/Array

"""
There are several method to reverse an List/Array

"""


# Using reverse() Method
def reverse_list(lst):
    lst.reverse()
    return lst

print(reverse_list([1, 2, 3, 4, 5]))


# Using Slicing
def slice_list(lst):
    reversed_list = lst[::-1]
    return reversed_list

print(slice_list([1, 2, 3, 4]))


# Using Loop
def reverse_array(lst):
    reversed_array = []
    for i in lst:
        reversed_array.insert(0, i)
    return reversed_array

print(reverse_array([1, 2, 3]))

        # Or

def reverse_lst(lst):
    reversed_lst = []
    for i in range(len(lst)-1,-1,-1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_lst([1, 2]))