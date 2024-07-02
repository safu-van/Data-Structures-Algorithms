# Remove duplicates from a singly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            

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
    
    # to check duplicate values and passed to delete_node_value() method for deleting the node.
    def remove_duplicates(self):
        seen = set()
        current_node = self.head
        while current_node:
            if current_node.data in seen:
                self.delete_node_value(current_node.data)
            else:
                seen.add(current_node.data)
            current_node = current_node.next
    

    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        


ll1 = LinkedList()
ll1.append(1)
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(2)
ll1.append(3)
ll1.show()
print()
ll1.remove_duplicates()
ll1.show()
