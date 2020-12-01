class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def __repr__(self):
        return str(self.slots)

    def hashing_func(self, key):
        return key % self.size

    def find_index(self, key):
        index = self.hashing_func(key)
        while self.slots[index] is not None and self.slots[index] != key:
            index = (index + 1) % self.size
        return index

    def insert(self, key):
        index = self.find_index(key)
        if self.slots[index] != key:
            self.slots[index] = key

    def search(self, key):
        i = self.find_index(key)
        if self.slots[i] is not None:
            return i


ht = HashTable(10)
ht.insert(40)
print(ht)
ht.insert(20)
print(ht)
ht.insert(10)
print(ht)
ht.insert(6)
print(ht)
ht.insert(8)
print(ht)
print(ht.search(40))
