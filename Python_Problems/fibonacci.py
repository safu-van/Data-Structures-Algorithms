# Print Fibonacci Sequence

"""
The Logic of Fibonacci is...

In fibonacci sequence the number n3 should be n1, n2.
    eg:- limit = 5
         result = [0, 1, 1, 2, 3]
            - how this works 0 + 1 is 1, 1 + 1 is 2, 1 + 2 is 3 ...

"""


def fibonacci(limit):
    result = []
    num1, num2 = 0, 1

    for _ in range(limit):
        result.append(num1)
        num1, num2 = num2, num1+num2

    return result

print(fibonacci(5))