# Find if the number is prime number or not using Recursion.

def is_prime(n, divisor=None):  # divisor is provided for dividing by the number "n"
    if divisor is None:
        divisor = n - 1
    
    if n <= 1:
        return False
    
    if divisor < 2:     # if divisor reach less than 2 then it is a prime number
        return True
    
    if n % divisor == 0:
        return False
    
    return is_prime(n, divisor-1)      # decrementing divisor and calling the function.


print(is_prime(4))