# Queue all operations.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    # to add node to rear of queue.
    def enqueue(self, data):
        new_node = Node(data)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.length += 1
    
    # to remove front node from queue.
    def dequeue(self):
        if self.front is None:
            print("empty")
        else:
            self.front = self.front.next
            self.length -= 1
            if self.front is None:
                self.rear = None
            
    # to print front node from queue.
    def peek(self):
        if self.front is None:
            print("empty")
        else:
            print(self.front.data)
    
    # to print the size of queue.
    def size(self):
        print(self.length)

    # to print the queue is empty or not.
    def is_empty(self):
        if self.front:
            print(False)
        else:
            print(True)
        
    # to print the queue.
    def show(self):
        current_node = self.front
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()



l1 = Queue()
l1.enqueue(1)
l1.show()
l1.dequeue()
l1.peek()
l1.size()
l1.is_empty()