# Selection Sort

array = [2, 5, 3, 6, 4, 7, 1]

for i in range(len(array)-1):

    min_value_index = i     # on first iteration assume array first element as min_value

    for j in range(i+1, len(array)):
        if array[j] < array[min_value_index]:   # if value is less then min_value then store min_value index.
            min_value_index = j

    """
        check if i not equal to min_value_index, if it is equal that means the array[min_value_index] is the min_value no need to swap.
    """
    if i != min_value_index:
        array[i], array[min_value_index] = array[min_value_index], array[i]


print(array)