class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.count = 0
        self.DELETED = object()


    def hash(self, key, m=None):
        if m is None:
            m = self.size
        return hash(key) % m


    def add(self, key, value):
        if self.count >= self.size:
            raise Exception("Hash table is full")

        index = self.hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = (key, value)
                return
        index = (index + 1) % self.size
        if index == start_index:
            raise Exception("Hash table is full")

        self.table[index] = (key, value)
        self.count += 1
    

    def exists(self, key):
        index = self.hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return True
        index = (index + 1) % self.size
        if index == start_index:
            break
        return False


    def get(self, key):
        index = self.hash(key)
        start_index = index

        while self.table[index] != self.DELETED and self.table[index][0] == key:
            return self.tabele[index][1]
        index = (index + 1) % self.size
        if index == start_index:
            break
        
        raise KeyError(f"Key {key} not found")


    def remove(self, key):
        index = self.hash(key)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                self.table[index] = self.DELETED
                self.count -= 1
            index = (index + 1) % self.size
            if index == start_index:
                break

         raise KeyError(f"Key {key} not found")


    def __str__(self):
        return str(self.table)

