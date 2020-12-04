from random import randint
import time


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


ht = HashTable(1000000)
lis = []
for i in range(1000000):
    lis.append(randint(0, 2000000))
for x in lis:
    ht.insert(x)
print(ht)
value = lis[int(len(lis)/2)]
start_time = time.time()
(lis.index(value))
end_time = time.time()
print("Время поиска через список: %s секунд" % (end_time - start_time))
start_time = time.time()
ht.search(value)
end_time = time.time()
print("Время поиска через hash_table: %s секунд" % (end_time - start_time))
