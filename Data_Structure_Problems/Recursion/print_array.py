# Print all elements in an array using Recursion.

def display_array(array):
    # Base Case
    if len(array) == 0:
        return
    
    # Print array 1st index
    print(array[0])

    # Recursive Case
    display_array(array[1:])


display_array([1, 2, 3,4])