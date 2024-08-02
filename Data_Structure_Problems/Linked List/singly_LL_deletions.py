# Singly Linked List all deletions.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # to delete node at the beginning
    def delete_the_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # to delete node at the specified index
    def delete_the_index(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            i = 0
            while current_node and i < index-1:
                current_node = current_node.next
                i += 1
            if current_node is None or current_node.next is None:
                print("index out of range")
            else:
                current_node.next = current_node.next.next
            
    # to delete node at the end
    def delete_the_end(self):
        if self.head.next is None:
            self.head = None
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    # to delete node of given value
    def delete_node_value(self, value):
        if self.head.data == value:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next
            print(f"{value} is not in list")
            
    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next



ll1 = LinkedList()
ll1.insert_at_beginning(4)
ll1.insert_at_beginning(3)
ll1.insert_at_beginning(2)
ll1.insert_at_beginning(1)
ll1.delete_the_beginning()
ll1.delete_the_index(2)
ll1.delete_the_end()
ll1.delete_node_value(5)
ll1.show()

