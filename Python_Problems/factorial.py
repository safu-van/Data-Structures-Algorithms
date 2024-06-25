# Get factorial

"""
The Logic of Factorial is...

Get the number.
Multiply from 1 to the number given.
the result is the factorial of the number.
    eg:- number = 5
         result = 1*2*3*4*5     

"""


def factorial(num):
    result = 1
    for num in range(1, num+1):
        result *= num
    return result

print(factorial(4))