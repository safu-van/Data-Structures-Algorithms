# Reverse a string using stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        for i in data:
            new_node = Node(i)

            if self.top is None:
                self.top = new_node
            else:
                new_node.next = self.top
                self.top = new_node
    

    def show(self):
        current_node = self.top

        while current_node:
            print(current_node.data, end="")
            current_node = current_node.next



l1 = Stack()
l1.push("hello")
l1.show()