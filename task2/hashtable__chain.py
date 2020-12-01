class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [[] for _ in range(size)]

    def __repr__(self):
        return str(self.slots)

    def hashing_func(self, key, slots):
        return key % len(slots)

    def insert(self, key, value):
        index = self.hashing_func(key, self.slots)
        key_exists = False
        bucket = self.slots[index]
        for i, key_value in enumerate(bucket):
            k, v = key_value
            if k is key:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hashing_func(key, self.slots)
        bucket = self.slots[hash_key]
        for i, key_value in enumerate(bucket):
            k, v = key_value
            if k is key:
                return v


tb = HashTable(5)
print(tb)
tb.insert(40, 'cat')
tb.insert(17, 'dog')
tb.insert(24, 'bull')
tb.insert(10, 'eagle')
print(tb)
print(tb.search(40))
