# Bubble Sort

array = [2, 5, 3, 6, 4, 7, 1]

for i in range(len(array)-1):
    swapped = False     # to check if the array is already sorted

    """
        we give -i because after every iteration an element will be sorted so no need to check it again.
    """
    for j in range(len(array)-1-i): 
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            swapped = True
    
    if not swapped:     # if not swapped then the array is sorted.
        break

print(array)
