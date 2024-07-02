# Find middle node of a Singly Linked List.


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
    

    # find middle node
    def middle(self):
        a = self.head
        b = self.head
        while b and b.next:
            a = a.next
            b = b.next.next
        print(a.data)    
    

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
ll1.middle()