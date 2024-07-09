# Convert Array to Singly Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    

    # Converting array to linked list
    def array_to_LL(self, array):
        new_node = Node(array[0])
        self.head = new_node

        current_node = self.head
        for data in array[1:]:
            new_node = Node(data)
            current_node.next = new_node
            current_node = current_node.next
    

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        


l1 = LinkedList()
l1.show()
l1.array_to_LL([1, 2, 3, 4, 5])
l1.show()

        

