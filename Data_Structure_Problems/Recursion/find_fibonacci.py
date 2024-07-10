# Print the fibonacci sequence using a recursion.

def fibonacci(n):
    # Base Case
    if n == 0 or n == 1:
        return n
    
    # Recursive Case
    return fibonacci(n-1) + fibonacci(n-2)


sequence = 10
for i in range(sequence):
    print(fibonacci(i))