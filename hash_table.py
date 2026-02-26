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

        while self.table[index] is not None:
            if self.table[index] != self.DELETED and self.table[index][0] == key:
                return self.table[index][1]
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
                return
            index = (index + 1) % self.size
            if index == start_index:
                break

        raise KeyError(f"Key {key} not found")


    def __str__(self):
        return str(self.table)




def run_tests():
    print("Creating hash table of size 5...")
    ht = HashTable(5)

    print("\n--- Test 1: Add elements ---")
    ht.add("apple", 1)
    ht.add("banana", 2)
    ht.add("cherry", 3)
    print("Table after inserts:", ht)

    print("\n--- Test 2: Get elements ---")
    print("apple:", ht.get("apple"))
    print("banana:", ht.get("banana"))
    print("cherry:", ht.get("cherry"))

    print("\n--- Test 3: Exists check ---")
    print("Exists 'apple':", ht.exists("apple"))
    print("Exists 'grape':", ht.exists("grape"))

    print("\n--- Test 4: Update existing key ---")
    ht.add("apple", 100)
    print("Updated apple:", ht.get("apple"))

    print("\n--- Test 5: Remove element ---")
    ht.remove("banana")
    print("Table after removing banana:", ht)
    print("Exists 'banana':", ht.exists("banana"))

    print("\n--- Test 6: Remove non-existing key (should raise error) ---")
    try:
        ht.remove("banana")
    except KeyError as e:
        print("Caught expected error:", e)

    print("\n--- Test 7: Get non-existing key (should raise error) ---")
    try:
        ht.get("banana")
    except KeyError as e:
        print("Caught expected error:", e)

    print("\n--- Test 8: Fill table until full ---")
    try:
        ht.add("date", 4)
        ht.add("elderberry", 5)
        ht.add("fig", 6)  # Should raise Exception (table full)
    except Exception as e:
        print("Caught expected error:", e)

    print("\nFinal table state:")
    print(ht)


if __name__ == "__main__":
    run_tests()
