# Check number is Prime or not

"""
The Logic of Prime Numbers is...

Get the number.
Prime number means,
The number should be greater than 1 and the number should only
divisible by 1 and itself, if then it is Prime Number.
    eg:- 2,3,5,7,11,13... are all prime numbers.

"""


def is_prime_number(num):
    if num <= 1:
        return f"{num} is not Prime Number"
    
    for i in range(2, num):     # if the num is 2 then the range(2, 2) means empty loop, the loop will not iterate.
        if num % i == 0:
            return f"{num} is not Prime Number"
    return f"{num} is Prime Number"


print(is_prime_number(13))
