class DynamicArray:
    def __init__(self):
        self.size = 0 
        self.capacity = 1
        self.data = self.makeArray(self.capacity) 
    
    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return self.size == 0

    def at(self, index):
        if not 0<= index < self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def insert(self, index, value):
        if not 0<= index < self.size:
            raise IndexError("Index out of bounds")

        if self.size == self.capacity:
            self.resize(2* self.capacity)
        
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
            
        self.data[index] = value
        self.size += 1            

    def append(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1

    def prepend(self, value):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)

        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]

        self.data[0] = value
        self.size += 1

    def remove(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                for j in range(i, self.size - 1):
                    self.data[j] = self.data[j + 1]
                self.data[self.size - 1] = None
                self.size -= 1

                return
        raise ValueError("Value not found")

    def push(self, value):
        self.append(value)

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty array") 

        value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1

        if 0 < self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

        return value

    def delete(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]

        self.data[self.size - 1]
        self.size -= 1

        if 0 < self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

    def find(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        return -1

    def makeArray(self, capacity):
        return [None] * capacity 

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def __str__(self):
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]" 




def run_tests():
    print("Running tests...")

    arr = DynamicArray()

    assert arr.isEmpty() == True
    assert len(arr) == 0

    arr.append(10)
    arr.append(20)
    arr.append(30)
    assert len(arr) == 3
    assert arr[0] == 10
    assert arr[1] == 20
    assert arr[2] == 30

    arr.push(40)
    assert arr[3] == 40
    assert len(arr) == 4

    arr.prepend(5)
    assert arr[0] == 5
    assert len(arr) == 5

    arr.insert(2, 15)
    assert arr[2] == 15

    assert arr.find(15) == 2
    assert arr.find(999) == -1

    arr.remove(15)
    assert arr.find(15) == -1

    old_size = len(arr)
    arr.delete(0)
    assert len(arr) == old_size - 1

    last = arr.pop()
    assert last == 40
    assert len(arr) == old_size - 2

    big = DynamicArray()
    for i in range(100):
        big.append(i)
    assert big.getSize() == 100
    assert big.getCapacity() >= 100

    for _ in range(90):
        big.pop()
    assert big.getSize() == 10
    assert big.getCapacity() >= big.getSize()

    try:
        arr.delete(100)
        assert False
    except IndexError:
        pass

    try:
        arr.remove(999)
        assert False
    except ValueError:
        pass

    try:
        empty = DynamicArray()
        empty.pop()
        assert False
    except IndexError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
