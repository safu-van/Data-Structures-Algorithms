# Merge Sort

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2       # find the middle of array
        left_array = array[:mid]    # from 1st element till middle-1 element
        right_array = array[mid:]   # from mid element to last element

        merge_sort(left_array)      # to recursively divide the left array
        merge_sort(right_array)     # to recursively divide the right array

        i = j = k = 0       # i for left_array, j for right_array, k for the main array.
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
                k += 1
            else:
                array[k] = right_array[j]
                j += 1
                k += 1
        
        """ if there element balance to add to main array from left_array then this loop will add them """
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        
        """ if there element balance to add to main array from right_array then this loop will add them """
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


array = [3, 2, 1, 5, 7, 4, 10]

merge_sort(array)
print(array)    