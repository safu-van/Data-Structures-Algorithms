# Doubly Linked List all insertions.


class Node:
    def __init__(self, data):
        self.prev = None
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
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # to insert node at the specified index.
    def insert_at_index(self, index, data):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        i = 0
        current_node = self.head
        while current_node and i < index-1:
            current_node = current_node.next
            i += 1

        if current_node is None:
            print("index out of range")
            return
        
        if current_node.next is None:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return
        
        new_node.next = current_node.next
        current_node.next.prev = new_node
        current_node.next = new_node
        new_node.prev = current_node
            
    # to insert node before the specified node.
    def insert_before_node(self, node_data, data):
        new_node = Node(data)

        if self.head.data == node_data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
        
        current_node = self.head
        while current_node:
            if current_node.data == node_data:
                break
            current_node = current_node.next

        if current_node is None:
            print(f"{node_data} not found in list")
            return
        
        current_node.prev.next = new_node
        new_node.prev = current_node.prev
        new_node.next = current_node
        current_node.prev = new_node

    # to insert node after the specified node.
    def insert_after_node(self, node_data, data):
        new_node = Node(data)
        
        if self.tail.data == node_data:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return
        
        current_node = self.head
        while current_node:
            if current_node.data == node_data:
                break
            current_node = current_node.next

        if current_node is None:
            print(f"{node_data} not found in list")
            return
        
        new_node.next = current_node.next
        current_node.next.prev = new_node
        new_node.prev = current_node
        current_node.next = new_node

    # to insert node at the end.
    def append(self, data):
        new_node = Node(data)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # to reverse print
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
list_1.insert_at_beginning(2)
list_1.insert_at_beginning(1)
list_1.insert_at_index(0, 0)
list_1.insert_at_index(3, 4)
list_1.insert_before_node(4, 3)
list_1.insert_after_node(4, 5)
list_1.append(6)
list_1.show()
print()
list_1.reverse_show()


