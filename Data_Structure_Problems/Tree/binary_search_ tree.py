# Binary Search Tree (BST)

class BST:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    # Insert node
    def insert(self, data):        
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)
    
    # Search node
    def contains(self, data):
        if self.data == data:
            print("Node found")
            return
        
        if data < self.data:
            if self.left:
                self.left.contains(data)
            else:
                print("Node not found")
        else:
            if self.right:
                self.right.contains(data)
            else:
                print("Node not found")

    # Pre-Order Traversal
    def pre_order(self):
        print(self.data, end=" ")

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()    

    # In-Order Traversal
    def in_order(self):
        if self.left:
            self.left.in_order()

        print(self.data, end=" ")

        if self.right:
            self.right.in_order()  
    
    # Post-Order Traversal
    def post_order(self):
        if self.left:
            self.left.post_order()
        
        if self.right:
            self.right.post_order()
        
        print(self.data, end=" ")
    
    # Level-Order Traversal
    def level_order(self):
        queue = []
        queue.append(self)

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    # Delete node
    def delete(self, data, root_data):        
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data, root_data)
            else:
                print(f"{data} node is not found")
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data, root_data)
            else:
                print(f"{data} node is not found")
        else:
            # Case 1 : Delete node with 0 child
            if self.left is None and self.right is None:
                return None

            # Case 2 : Delete node with 1 child
            if self.left is None:
                """ when deleting root node with 1 child do this """
                if data == root_data:
                    self.data = self.right.data
                    self.left = self.right.left
                    self.right = self.right.right
                    return
                return self.right
            elif self.right is None:
                """ when deleting root node with 1 child do this """
                if data == root_data:
                    self.data = self.left.data
                    self.left = self.left.left
                    self.right = self.left.right
                    return
                return self.left                
            
            # Case 3 : Delete node with 2 child
            node = self.right
            while node.left:
                node = node.left
            self.data = node.data
            self.right = self.right.delete(node.data, root_data)

        return self

    def min(self):
        node = self
        while node.left:
            node = node.left
        return node.data
    
    def max(self):
        node = self
        while node.right:
            node = node.right
        return node.data
    


root = BST(10)

root.insert(20)
root.insert(30)
root.insert(2)

root.contains(2)

print("Pre-Order :", end=" ")
root.pre_order()
print()

print("In-Order :", end=" ")
root.in_order()
print()

print("Post-Order :", end=" ")
root.post_order()
print()

print("Level-Order :", end=" ")
root.level_order()
print()

root.delete(10, root.data)
root.pre_order()
print()

print(f"min element {root.min()}")
print(f"max element {root.max()}")

    
