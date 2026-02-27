from dynamic_array import DynamicArray

class MaxHeap(DynamicArray):
    def __init__(self):
        super().__init__() 

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1

    def right(self, index):
        return 2 * index + 2

    def insert(self, value):
        self.append(value) 
        self.sift_up(self.size - 1)

    def sift_up(self, index):
        while index > 0 and self.data[self.parent(index)] < self.data[index]:
            parent_index = self.parent(index)
            self.data[parent_index], self.data[index] = self.data[index], self.data[parent_index]
            index = parent_index

    def get_max(self):
        if self.isEmpty():
            raise IndexError("Heap is empty")
        return self.data[0]

    def get_size(self):
        return self.size 
        
    def is_empty(self):
        return self.size == 0 

    def extract_max(self):
        if self.isEmpty():
            raise IndexError("Heap is empty")
        
        max_value = self.data[0]

        self.data[0] = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        if self.size > 0:
            self.sift_down(0)

        return max_value


    def sift_down(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < self.size and self.data[left] > self.data[largest]:
                largest = left

            if right < self.size and self.data[right] > self.data[largest]:
                largest = right

            if largest == index:
                break

            self.data[index], self.data[largest] = self.data[largest], self.data[index]
            index = largest


    def remove(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Index out of bounds")
        
        self.data[index] = float('inf')
        self.sift_up(index)

        self.extract_max()


    def heapify(self, array):
        self.size = 0
        self.capacity = max(1, len(array))
        self.data = self.makeArray(self.capacity)

        for value in array:
            self.append(value)

        for i in range((self.size // 2) - 1, -1, -1):
            self.sift_down(i)


    def heap_sort(self, array):
        self.heapify(array)

        end = self.size - 1
        while end > 0:
            self.data[0], self.data[end] = self.data[end], self.data[0]
            self.size -= 1
            self.sift_down(0)
            end -= 1

        self.size = len(array)

        for i in range(len(array)):
            array[i] = self.data[i]

        return array


def run_tests():
    print("Running MaxHeap tests...")

    heap = MaxHeap()
    assert heap.is_empty() == True
    assert heap.get_size() == 0

    heap.insert(10)
    heap.insert(40)
    heap.insert(20)
    heap.insert(5)
    heap.insert(60)

    assert heap.get_max() == 60
    assert heap.get_size() == 5
    assert heap.is_empty() == False

    max_val = heap.extract_max()
    assert max_val == 60
    assert heap.get_max() == 40
    assert heap.get_size() == 4

    results = []
    while not heap.is_empty():
        results.append(heap.extract_max())

    assert results == [40, 20, 10, 5]

    heap = MaxHeap()
    for value in [50, 30, 40, 10, 20, 35]:
        heap.insert(value)

    heap.remove(2)
    assert heap.get_size() == 5

    prev = heap.extract_max()
    while not heap.is_empty():
        current = heap.extract_max()
        assert prev >= current
        prev = current

    heap = MaxHeap()
    array = [3, 9, 2, 1, 4, 5]
    heap.heapify(array)

    assert heap.get_max() == 9

    sorted_desc = []
    while not heap.is_empty():
        sorted_desc.append(heap.extract_max())

    assert sorted_desc == [9, 5, 4, 3, 2, 1]

    heap = MaxHeap()
    array = [12, 3, 17, 8, 34, 25, 1]

    sorted_array = heap.heap_sort(array)

    assert sorted_array == sorted([12, 3, 17, 8, 34, 25, 1])
    assert array == sorted([12, 3, 17, 8, 34, 25, 1])

    heap = MaxHeap()

    try:
        heap.get_max()
        assert False
    except IndexError:
        pass

    try:
        heap.extract_max()
        assert False
    except IndexError:
        pass

    try:
        heap.remove(0)
        assert False
    except IndexError:
        pass

    import random

    heap = MaxHeap()
    values = list(range(1000))
    random.shuffle(values)

    for v in values:
        heap.insert(v)

    extracted = []
    while not heap.is_empty():
        extracted.append(heap.extract_max())

    assert extracted == sorted(values, reverse=True)

    print("All MaxHeap tests passed successfully!")


if __name__ == "__main__":
    run_tests()
