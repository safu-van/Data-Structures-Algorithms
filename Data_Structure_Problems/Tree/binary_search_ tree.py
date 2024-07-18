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
    def search(self, data):
        if self.data == data:
            print("Node found")
            return
        
        if data < self.data:
            if self.left:
                self.left.search(data)
            else:
                print("Node not found")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node not found")


root = BST(10)

root.insert(20)
root.insert(30)
root.insert(2)

root.search(2)
root.search(5)


    
