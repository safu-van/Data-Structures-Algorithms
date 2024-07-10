# Find factorial of a given number using Recursion.

def factorial(n):
    # Base Case
    if n == 1:
        return n
    
    # Recursive Case
    return factorial(n-1) * n

factorial_of_5 = factorial(5)
print(factorial_of_5)