# Heap Sort

def shift_down(array, idx, size):
    last_idx = size - 1
    left_child = 2 * idx + 1

    while left_child <= last_idx:
        right_child = 2 * idx + 2
        
        if right_child <= last_idx and array[right_child] > array[left_child]:
            idx_to_shift = right_child
        else:
            idx_to_shift = left_child
        
        if array[idx_to_shift] > array[idx]:
            array[idx], array[idx_to_shift] =  array[idx_to_shift], array[idx]
            idx = idx_to_shift
            left_child = 2 * idx + 1
        else:
            return

def heap_sort(array):
    size = len(array)
    parent_idx = (size - 1) // 2
    while parent_idx >= 0:
        shift_down(array, parent_idx, size)
        parent_idx -= 1
    
    for i in range(size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        shift_down(array, 0, i)



array = [2, 3, 10, 5, 15, 20, 50]
print("before sorting :", array)

heap_sort(array)

print("after sorting :", array)