# Find sum of the numbers till the given number.

def find_sum(n):
    # Base Case
    if n == 1:
        return n
    
    # Recursive Case
    return find_sum(n-1) + n


sum = find_sum(5)
print(sum)