# Quick Sort


# to place pivot on the right position in array.
def partion(array, first, last):
    pivot = array[first]    # Taking first element as pivot
    left = first + 1
    right = last

    while True:
        while left <= right and array[left] <= pivot:
            left += 1
        
        while left <= right and array[right] >= pivot:
            right -= 1

        if right < left:
            break
        else:
            array[left], array[right] = array[right], array[left]

    array[first], array[right] = array[right], array[first]
    return right    # return pivot index


def quick_sort(array, first, last):
    if first < last:
        pivot_index = partion(array, first, last)
        quick_sort(array, first, pivot_index-1)     # To quick sort recursively the left side of array
        quick_sort(array, pivot_index+1, last)      # To quick sort recursively the right side of array



array = [4, 3, 9, 8, 2, 1]
first = 0
last = len(array) - 1

# it will sort in ascending order
quick_sort(array, first, last)
print(array)

"""
To Sort in descending order in partion method change the while loop condition :-

    "while left <= right and array[left] <= pivot" change to "while left <= right and array[left] >= pivot"
                                         ^                                                        ^
                                                  and

    "while left <= right and array[right] >= pivot" change to "while left <= right and array[right] <= pivot"
                                          ^                                                         ^
"""