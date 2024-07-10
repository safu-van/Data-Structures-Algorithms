# Find the target element index using Binary Serach.
""" To do binary search the array should be a sorted array """

array = [1, 2, 3, 4, 5]
target = 2

i = 0
j = len(array)-1                                                                 
while i <= j:
    mid = (i + j) // 2

    if array[mid] == target:
        print(f"targe {target} is in index {mid}")
        break
    else:
        if array[mid] > target:
            j = mid -1
        else:
            i = mid +1
            
else:
    print(f"target {target} not found")




