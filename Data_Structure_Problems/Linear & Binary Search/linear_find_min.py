# Find min element from an array.

array = [1, -2, -1, 0, 5]

min_element = array[0]  # assign array first element as min element 

for value in array:
    if value < min_element:     # if the value is less than min element then replace min element
        min_element = value

print(min_element)