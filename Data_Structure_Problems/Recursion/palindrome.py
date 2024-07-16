# Check the string is palindrome or not.

def palindrome(str):
    # Base Case
    if len(str) <= 1:
        return True
    
    # Recursive Case
    if str[0] == str[-1]:
        return palindrome(str[1:-1])
    else:
        return False


print(palindrome("malayalam"))