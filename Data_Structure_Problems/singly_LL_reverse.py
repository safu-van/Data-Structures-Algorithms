# Reverse a Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    

    def insert_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    

    # reverse a linked list
    def reverse(self):                      
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
    

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        


ll1 = LinkedList()
ll1.insert_to_beginning(3)
ll1.insert_to_beginning(2)
ll1.insert_to_beginning(1)
ll1.show()
print()
ll1.reverse()
ll1.show()