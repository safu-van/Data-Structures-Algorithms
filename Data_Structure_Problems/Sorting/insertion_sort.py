# Insertion Sort

array = [1, 2, 3, 4, 3, 2, 1]

for i in range(1, len(array)):      # will start from 2nd element.
    current = array[i]
    
    j = i - 1
    while j >= 0 and current < array[j]:    # if array is sorted this loop will not work.
        array[j+1] = array[j]
        j -= 1

    array[j+1] = current


print(array)
