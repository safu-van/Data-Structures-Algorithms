# Find the missing number in List/Array.


def find_missing(lst):
    missing_numbers = []

    for i in range(len(lst)-1):
        diff = lst[i+1] - lst[i]

        if diff > 1:
            for num in range(lst[i]+1, lst[i+1]):
                missing_numbers.append(num)

    return missing_numbers

print(find_missing([1,4,10]))

    # Or

def show_missing(lst):
    missing_numbers = []
    start = min(lst)
    end = max(lst)

    for i in range(start, end):
        if i not in lst:
            missing_numbers.append(i)
    
    return missing_numbers

print(show_missing([1,5,15]))


