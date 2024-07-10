# From a sorted array find the target index if the target is not found then give the index were it would be if inserted in order.

array = [1, 2, 3, 5, 6]
target = 4

i, j = 0, len(array)-1
while i <= j:
    mid = (i+j) // 2

    if array[mid] == target:
        print(f"target found on index {mid}")
        break
    else:
        if array[mid] > target:
            j = mid - 1
        else:
            i = mid + 1

else:
    print(f"target is not found, if it is inserted it would be on index {i}")