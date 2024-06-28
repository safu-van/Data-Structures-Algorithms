# Check number is Armstrong or not

"""
The Logic of Armstrong is...

Get the number.
Take the number digits count.
sum all the digits raised with power of digits count.
and check if the provided number and sum is equal, if then it is Armstrong Number.
    eg:- number = 153
         result = 1*1*1 + 5*5*5 + 3*3*3   # digits raised to its power which here the digits count is 3.

"""


def is_armstrong(num):
    num_str = str(num)
    digits_count = len(num_str)
    result = 0

    for digit in num_str:
        result += int(digit) ** digits_count

    if num == result:
        return f"{num} is armstrong"
    return f"{num} is not armstrong"
        

print(is_armstrong(124))