# Doubly Linked List all deletions.


class Node:
    def __init__(self, data):
        self.prev = None
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
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    

    # to delete node at the beginning.
    def delete_the_beginning(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return 

        self.head = self.head.next
        self.head.prev = None

    
    # to delete node at the specified index.
    def delete_the_index(self, index):
        if index == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        
        i = 0
        current_node = self.head
        while current_node and i < index:
            current_node = current_node.next
            i += 1
        
        if current_node is None:
            print("index out of range")
            return

        if current_node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev


    # to delete node at the end.
    def delete_the_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        self.tail = self.tail.prev
        self.tail.next = None
                

    # to delete node of given value.
    def delete_node_value(self, value):
        if self.head.data == value:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return 
        
        current_node = self.head
        while current_node and current_node.data != value:
            current_node = current_node.next
        
        if current_node is None:
            print(f"{value} is not in list")
            return
        
        if current_node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev


    def reverse_show(self):
        current_node = self.tail 
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.prev


    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next



list_1 = LinkedList()
list_1.insert_at_beginning(3)
list_1.insert_at_beginning(2)
list_1.insert_at_beginning(1)
list_1.show()
print()
list_1.delete_node_value(4)
list_1.show()
print()
list_1.reverse_show()

    