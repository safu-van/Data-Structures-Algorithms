# Hash Table

class HashTable:
    def __init__(self, size):
        self.size = size
        self.array = [None for _ in range(self.size)]
    
    # hash function.
    """
        it receives the key and find the ascii value of each character and sum it all,
        then modulos the sum by the size of the array and return.

    """
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)   # ord() method is used to find ascii value.
        return hash % self.size
    
    # to add key, value to hash table.
    def add(self, key, value):
        hash = self.get_hash(key)
        self.array[hash] = value
    
    # to get value using key in hash table.
    def get(self, key):
        hash = self.get_hash(key)
        print(self.array[hash])
    
    # to delete.
    def delete(self, key):
        hash = self.get_hash(key)
        self.array[hash] = None



h1 = HashTable(10)
h1.add("name", "safuvan")
h1.add("name", "safuan")
h1.add("age", 18)
h1.get("name")
