# Stack all operations.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    # to add node to top of stack.
    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1
    
    # to remove top node from stack.
    def pop(self):
        if self.top is None:
            print("stack underflow")
        else:
            self.top = self.top.next
            self.length -= 1
    
    # to print top node data from stack.
    def peek(self):
        if self.top is None:
            print("stack underflow")
        else:
            print(self.top.data)
    
    # to print the size of stack.
    def size(self):
        print(self.length)
    
    # to print the stack is empty or not.
    def is_empty(self):
        if self.top:
            print(False)
        else:
            print(True)
    
    # to print the stack.
    def show(self):
        current_node = self.top
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()



l1 = Stack()
l1.push(1)
l1.show()
l1.pop()
l1.peek()
l1.size()
l1.is_empty()