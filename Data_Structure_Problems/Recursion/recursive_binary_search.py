# Binary Search using Recursion

def recursive_binary(array, start, end, target):
    if start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return f"target found on index {mid}"
        else:
            if array[mid] < target:
                start = mid + 1
                return recursive_binary(array, start, end, target)
            else:
                end = mid - 1
                return recursive_binary(array, start, end, target)
    else:
        return "target not found"
    

array = [1, 2, 3, 4, 5]
target = 3
start = 0
end = len(array)-1

print(recursive_binary(array, start, end, target))