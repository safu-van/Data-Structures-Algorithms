# Basic Singly Linked list Structure with inserting node at the end and display list methods.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # to insert node at the end.
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
    
    # to print the list.
    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
    

list_1 = LinkedList()
list_1.append(1)
list_1.append(2)
list_1.append(3)
list_1.show()

