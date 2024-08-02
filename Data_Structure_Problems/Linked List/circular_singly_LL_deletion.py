# Circular Singly Linked List Deletions.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        
        new_node.next = self.head
        self.head = new_node
        self.tail.next = self.head

    # to delete node at the beginning
    def delete_the_beginning(self):
        if self.head is None:
            print("empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next
        self.tail.next = self.head
    
    # to delete node at the end
    def delete_the_end(self):
        if self.head is None:
            print("empty")
            return
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next
        self.tail = current_node
        self.tail.next = self.head

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            if current_node.next == self.head:
                return
            current_node = current_node.next



l1 = LinkedList()
l1.insert_at_beginning(1)
l1.insert_at_beginning(2)
l1.insert_at_beginning(3)
l1.insert_at_beginning(4)
l1.show()
print()
l1.delete_the_beginning()
l1.delete_the_end()
l1.show()
