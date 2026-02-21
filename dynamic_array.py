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

    def remove(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                for j in range(i, self.size - 1):
                    self.data[j] = self.data[j + 1]
                self.data[self.size - 1] = None
                self.size -= 1

                return
        raise ValueError("Value not found")


    def pop(self):
        if self.size == 0:
            return IndexError("Pop from empty array") 

        value = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1

        return value

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



if __name__=="__main__":
    arr = DynamicArray()
    arr.append(10)
    arr.append(20)
    arr.append(30)

    print(arr)
    arr.insert(1, 15)
    print(arr)

    arr.remove(20)
    print(arr)

    print(arr.pop())
    print(arr)


