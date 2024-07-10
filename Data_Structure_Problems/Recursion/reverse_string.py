# Reverse a string using Recursion.

def reverse_str(str):
    # Base Case
    if len(str) == 1:
        return str
    
    # Recursive Case
    return reverse_str(str[1:]) + str[0]


reversed_str = reverse_str("safuvan")
print(reversed_str)
