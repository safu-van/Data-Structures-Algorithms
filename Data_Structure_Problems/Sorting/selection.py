array = [3, 2, 1]

for i in range(len(array)-1):
    for j in range(i, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)