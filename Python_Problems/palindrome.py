# Check Palindrome or not

"""
The Logic of Palindrome is...

Palindrome means if the number, word, sentence any of them
read backwards and forwards it will be same.
    eg:- "malayalam", 1551  are palindrome.

"""


def is_palindrome(x):
    data = str(x)

    start = 0
    end = len(data) - 1
    while start < end:
        if data[start] != data[end]:
            return f"{data} is not Palindrome"
        start += 1
        end -= 1
    return f"{data} is Palindrome"


print(is_palindrome("malayalam"))


# Using Slicing
def is_pal(x):
    data = str(x)

    if data == data[::-1]:
        return f"{data} is Palindrome"
    return f"{data} is not Palindrome"

print(is_pal(123))


# Using reverse() Method
def is_pali(x):
    data = str(x)

    if list(data) == list(reversed(data)):
        return f"{data} is Palindrome"
    return f"{data} is not Palindrome"

print(is_pali("madam"))