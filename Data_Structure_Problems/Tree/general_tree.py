# General Tree


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    # To Add Child
    def add_child(self, data):
        data.parent = self
        self.child.append(data)


    """ to find that the node is in which level so as i want to put space in front before printing """
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level
    

    def print(self):
        space = " " * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        """ prefix is combination of space and "|__" it is just for understanding the parent and child while printing """
        print(prefix + self.data)
        if self.child:
            for child in self.child:
                child.print()


india_root = TreeNode("India")
kerala = TreeNode("Kerala")
tamilnadu = TreeNode("Tamilnadu")
mumbai = TreeNode("Gujarat")

india_root.add_child(kerala)
india_root.add_child(tamilnadu)
india_root.add_child(mumbai)

kerala.add_child(TreeNode("Malappuram"))
kerala.add_child(TreeNode("Thrissur"))

tamilnadu.add_child(TreeNode("Perambalur"))
tamilnadu.add_child(TreeNode("Chennai"))

mumbai.add_child(TreeNode("Ahmedabad"))
mumbai.add_child(TreeNode("Gandhinagar"))

# print the tree
india_root.print()



