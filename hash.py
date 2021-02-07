# Implement a hash table with get, set and remove function.

""" 
    Complexity:
    Space: O(1)
    Time: O(1)
"""

class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self.hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return 
            self.table[hash_index].append(Item(key, value))
    
    def get(self, key):
        hash_index = self.hash_function(key)
        for item in self.table[has_index]:
            if item.key == key:
                return item.value = value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self.hash_function(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return 
        raise KeyError('Key not Found')



