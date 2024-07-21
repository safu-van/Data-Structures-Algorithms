# Min-Heap 

class MinHeap:
    def __init__(self):
        self.heap = []
    
    # build heap from given array
    def build_heap(self, array):
        self.heap = array
        last_idx = len(self.heap) -1
        parent_idx = (last_idx - 1) // 2

        while parent_idx >= 0:
            self.shift_down(parent_idx)
            parent_idx -= 1
    
    def shift_down(self, idx):
        last_idx = len(self.heap) -1
        left_child = 2 * idx + 1

        while left_child <= last_idx:
            right_child = 2 * idx + 2

            if right_child <= last_idx and self.heap[right_child] < self.heap[left_child]:
                idx_to_shift = right_child
            else:
                idx_to_shift = left_child

            if self.heap[idx] > self.heap[idx_to_shift]:
                self.heap[idx], self.heap[idx_to_shift] = self.heap[idx_to_shift], self.heap[idx]
                idx = idx_to_shift
                left_child = 2 * idx + 1
            else:
                return
    
    def shift_up(self, idx):
        parent_idx = (idx - 1) // 2

        while idx > 0 and self.heap[parent_idx] > self.heap[idx]:
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            idx = parent_idx
            parent_idx = (idx - 1) // 2
    
    def delete(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.shift_down(0)
    
    # to show the min-element
    def peek(self):
        print(self.heap[0])

    def insert(self, data):
        self.heap.append(data)
        self.shift_up(len(self.heap)-1)

    def print(self):
        print(self.heap)



a = MinHeap()
a.build_heap([6, 2, 8])
a.print()
a.insert(1)
a.insert(5)
a.insert(15)
a.print()
a.delete()
a.print()
a.peek()