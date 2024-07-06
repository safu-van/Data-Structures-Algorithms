array = [1, 2, 3 ,4, 3, 2, 1]

for i in range(1, len(array)):
    temp = array[i]
    j = i-1
    while j >= 0 and temp < array[j]:
        array[j+1] = array[j]
        j = j -1
    array[j+1] = temp

print(array)
