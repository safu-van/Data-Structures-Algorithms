# Binary Search Tree (BST)

class BST:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    # Insert node
    def insert(self, data):
        if self.data is None:
            self.data = data
            return 
        
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
    
    # Delete node
    def delete(self, data):
        if self.data is None:
            print("Tree is empty")
            return
        
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print(f"{data} node is not found")
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print(f"{data} node is not found")
        else:
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            node = self.right
            while node.left:
                node = node.left
            self.data = node.data
            self.right = self.right.delete(node.data)
        return self



root = BST(10)

root.insert(20)
root.insert(30)
root.insert(2)

root.contains(2)
root.contains(5)

print("Pre-Order :", end=" ")
root.pre_order()
print()

print("In-Order :", end=" ")
root.in_order()
print()

print("Post-Order :", end=" ")
root.post_order()
print()

root.delete(10)
root.delete(20)
root.pre_order()

    
