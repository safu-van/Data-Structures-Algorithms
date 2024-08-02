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
    
    # to remove duplicate values
    def remove_duplicates(self):
        seen = set()
        prev_node = None
        current_node = self.head

        while current_node:
            if current_node.data in seen:
                if current_node.next:
                    prev_node.next = current_node.next
                    current_node = prev_node
                else:
                    prev_node.next = None
            else:
                seen.add(current_node.data)
            prev_node = current_node
            current_node = current_node.next
    
    def show(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        


ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(1)
ll1.append(1)
ll1.append(2)
ll1.append(2)
ll1.append(1)
ll1.show()
print()
ll1.remove_duplicates()
ll1.show()
