from linked_list import LinkedListWithTail
from linked_list import Node
from dynamic_array import DynamicArray


class LinkedListQueue(LinkedListWithTail):
    def enqueue(self, value):
        self.push_back(value) 

    def dequeue(self):
        return self.pop_front() 
    
    def empty(self):
        return self._size == 0 


class DynamicArrayQueue(DynamicArray):

    def enqueue(self, value):
        self.append(value) 


    def dequeue(self):
        if self.size == 0:
            raise IndexError("Dequeue from empty queue")
        value = self.at(0)
        
        for i in range(1, self.size):
            self.data[i - 1] = self.data[i]
        
        self.data[self.size - 1]
        self.size -= 1

        if 0 < self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)

        return value


    def empty(self):
        return self.size == 0 


    def full(self):
        return self.size == self.capacity 




def test_queue():
    q = DynamicArrayQueue()

    print("Running Dynamic Array Queue tests...")
    assert q.empty() == True

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    assert q.dequeue() == 10
    assert q.dequeue() == 20

    q.enqueue(40)

    assert q.dequeue() == 30
    assert q.dequeue() == 40

    assert q.empty() == True

    print("Dynamic array queue tests passed!")

    print("Running Linked List Queue tests...")

    q = LinkedListQueue()

    assert q.empty() == True
    assert q.size() == 0

    q.enqueue(10)
    assert q.empty() == False
    assert q.size() == 1
    assert q.front() == 10
    assert q.back() == 10

    q.enqueue(20)
    q.enqueue(30)

    assert q.size() == 3
    assert q.front() == 10
    assert q.back() == 30

    assert q.dequeue() == 10
    assert q.size() == 2
    assert q.front() == 20

    assert q.dequeue() == 20
    assert q.size() == 1
    assert q.front() == 30
    assert q.back() == 30

    q.enqueue(40)
    assert q.size() == 2
    assert q.front() == 30
    assert q.back() == 40

    assert q.dequeue() == 30
    assert q.dequeue() == 40

    assert q.empty() == True
    assert q.size() == 0

    try:
        q.dequeue()
        assert False
    except Exception:
        pass

    print("Linked list queue tests passed!")



if __name__=="__main__":
    test_queue()
