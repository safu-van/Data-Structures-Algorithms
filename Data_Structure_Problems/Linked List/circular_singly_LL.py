# Circular Singly Linked List Insertions.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    # to insert node at the beginning.
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
    

    # to insert node before the specified node.
    def insert_before_node(self, node_data, data):
        new_node = Node(data)

        if self.head.data == node_data:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
            return
        
        current_node = self.head
        while current_node.next != self.head:
            if current_node.next.data == node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        print(f"{node_data} not found in list")

    
    # to insert node after the specified node.
    def insert_after_node(self, node_data, data):
        new_node = Node(data)
        
        if self.tail.data == node_data:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            return
        
        current_node = self.head
        while current_node.next != self.head:
            if current_node.data == node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        print(f"{node_data} is not in the list")


    # to insert node at the end.
    def append(self, data):
        new_node = Node(data)

        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head


    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            if current_node.next == self.head:
                return
            current_node = current_node.next



l1 = LinkedList()
l1.insert_at_beginning(3)
l1.insert_at_beginning(2)
l1.insert_at_beginning(1)
l1.append(7)
l1.insert_after_node(7, 99)
l1.show()