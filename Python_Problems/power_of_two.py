# Check the given number is power of two or not.


def is_power_of_two(num):
    while num > 1:
        if num % 2 != 0:
            return False
        num = num / 2
    
    return True


print(is_power_of_two(2))
print(is_power_of_two(6))
print(is_power_of_two(1))