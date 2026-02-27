class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 


class LinkedList:
    def __init__(self):
        self._size = 0
        self.head = None

    def size(self):
        return self._size 

    def empty(self):
        return self._size == 0

    def value_at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range.")
        current = self.head 
        for i in range(index):
            current = current.next     
        return current.data  

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def push_back(self, value):
        new_node = Node(value)  

        if self.empty():
            self.head = new_node  
        else:
            current = self.head
            while current.next:
                current = current.next 
            current.next = new_node

        self._size += 1
                

    def pop_back(self):
        if self.empty():
           raise Exception("List is empty.") 

        if self._size == 1:
            value = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            value = current.next.data
            current.next = None

        self._size -= 1
        return value


    def front(self):
        if self.empty():
            raise Exception("List is empty")
        return self.head.data


    def back(self):
        if self.empty():
            raise Exception("List is empty")

        current = self.head
        while current.next:
            current = current.next
        return current.data


    def insert(self, index, value):
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        if index == 0:
            self.push_front(value)
            return
        
        new_node = Node(value)
        current = self.head

        for i in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self._size += 1


    def erase(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next

        self._size -= 1
        
    def value_n_from_end(self, n):
        if n < 0 or n >= self._size:
            raise IndexError("Index out of range")
        
        fast = self.head
        slow = self.head

        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        return slow.data

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def remove_value(self, value):
        if self.empty():
            return
        
        if self.head.data == value:
            self.head = self.head.next
            self._size -= 1
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next

class LinkedListWithTail:
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self._size == 0:
            self.tail = new_node

        self._size += 1

    def push_back(self, value):
        new_node = Node(value)

        if self.empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def pop_front(self):
        if self.empty():
            raise Exception("List is empty")

        value = self.head.data
        self.head = self.head.next
        self._size -= 1

        if self._size == 0:
            self.tail = None

        return value

    def front(self):
        if self.empty():
            raise Exception("List is empty")
        return self.head.data

    def back(self):
        if self.empty():
            raise Exception("List is empty")
        return self.tail.data



def run_tests():
    ll = LinkedList()
    assert ll.empty() == True
    assert ll.size() == 0

    ll.push_front(10)
    ll.push_front(5)
    assert ll.front() == 5
    assert ll.size() == 2

    ll.push_back(20)
    ll.push_back(30)
    assert ll.back() == 30
    assert ll.size() == 4

    assert ll.value_at(0) == 5
    assert ll.value_at(1) == 10
    assert ll.value_at(2) == 20
    assert ll.value_at(3) == 30

    ll.erase(2)
    assert ll.value_at(2) == 30
    assert ll.size() == 3

    assert ll.value_n_from_end(0) == 30
    assert ll.value_n_from_end(1) == 10
    assert ll.value_n_from_end(2) == 5

    ll.remove_value(20)
    assert ll.size() == 3
    assert ll.value_at(2) == 30

    ll.reverse()
    assert ll.value_at(0) == 30
    assert ll.value_at(1) == 10
    assert ll.value_at(2) == 5

    value = ll.pop_back()
    assert value == 5
    assert ll.size() == 2

    assert ll.front() == 30
    assert ll.back() == 10

if __name__=="__main__":
    run_tests()

