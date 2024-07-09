# Find max element from an array.

array = [1, 3, 1, 4, 4, 5, 6, 6]

max_element = array[0]  # assign array first element as max element 

for value in array:
    if value > max_element:     # if the value is greater than max element the replace max element
        max_element = value

print(max_element)