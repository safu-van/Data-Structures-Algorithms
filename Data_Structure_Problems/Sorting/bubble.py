array = [1,2,4, 2, 3, 5]

for i in range(len(array)-1):
    swapped = False
    for j in range(len(array)-1-i):
        print(j)
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            swapped = True
        
print(f"final array {array}")
