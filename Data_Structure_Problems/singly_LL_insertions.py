# Singly Linked List all insertions.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    # to insert node at the beginning.
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # to insert node at the specified index
    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            i = 0
            while current_node and i < index-1:
                current_node = current_node.next
                i += 1
            if current_node is None:
                print("index out of range")
            else:
                new_node.next = current_node.next
                current_node.next = new_node


    # to insert node before the specified node.
    def insert_before_node(self, node_data, data):
        new_node = Node(data)
        if self.head.data == node_data:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                if current_node.next.data == node_data:
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return
                current_node = current_node.next
            print(f"{node_data} is not in the list")
    

    # to insert node after the specified node.
    def insert_after_node(self, node_data, data):
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == node_data:
                new_node.next = current_node.next
                current_node.next = new_node
                return 
            current_node = current_node.next
        print(f"{node_data} is not in the list")
    

    # to insert node at the end.
    def append(self, data):
        new_node = Node(data)
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
list_1.insert_at_beginning(0)
list_1.append(1)
list_1.append(2)
list_1.insert_at_index(3, 3)
list_1.insert_after_node(3, 5)
list_1.insert_before_node(5, 4)
list_1.show()
