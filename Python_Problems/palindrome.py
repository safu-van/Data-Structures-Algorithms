# Check Palindrome or not

"""
The Logic of Palindrome is...

Palindrome means if the number, word, sentence any of them
read backwards and forwards it will be same.
    eg:- "malayalam", 1551  are palindrome.

"""


def is_palindrome(x):
    data = str(x)
    data = data.replace(" ","")
    data = data.lower()

    start = 0
    end = len(data) - 1
    while start < end:
        if data[start] != data[end]:
            return f"{data} is not Palindrome"
        start += 1
        end -= 1
    return f"{data} is Palindrome"


print(is_palindrome(1551))