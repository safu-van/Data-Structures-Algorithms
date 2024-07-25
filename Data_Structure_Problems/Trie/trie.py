class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # to insert the string.
    def insert(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    # to search if the string present in trie.
    def search(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    # to search if there any string starting with the given prefix.
    def startswith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    """ 
    to delete a string from trie actually it is not deleting,
    the is_end is set to false of that string so while searching it will return False

    """
    def delete(self, string):
        node = self.root
        for char in string:
            if char not in node.children:
                return f"{string} not found."
            node = node.children[char]
        node.is_end = False
        return f"{string} deleted."



a = Trie()
a.insert("apple")
a.insert("app")
a.insert("a")
print(a.search("apple"))
print(a.startswith("a"))
print(a.delete("apple"))
print(a.search("apple"))



"""
in trie node is_end is given as a boolean value instead i can set as 0 and when a word is completly added i can increment so it will be 1,
when the same word added twice then we can just increment the is_end to 2 and while deleting the word just decrement it,
so if a word is added twice then while delete it once still show when searching because it count is 1 so we have to delete it twice.

"""
