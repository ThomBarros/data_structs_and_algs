

def quick_sort(array, low, high):
    if low >= 0 and low < high:
        less_than, greater_than = partition(array, low, high)
        quick_sort(array, low, less_than - 1)
        quick_sort(array, greater_than + 1, high) 

def partition(array, low, high):
    pivot = array[(low + high) // 2]

    less_than = low
    equal_to = low
    greater_than = high

    while equal_to <= greater_than:
        if array[equal_to] < pivot:
            swapper = array[equal_to]
            array[equal_to] = array[less_than]
            array[less_than] = swapper
            less_than += 1
            equal_to += 1

        elif array[equal_to] > pivot:
            swapper = array[equal_to]
            array[equal_to] = array[greater_than]
            array[greater_than] = swapper
            greater_than -= 1
        
        else:
            equal_to += 1

    return less_than, greater_than



def run_tests():
    array = [2, 6, 4, 9 ,7, 1, 0, 5, 3, 8]
    print(array)
    quick_sort(array, 0, len(array) - 1)
    print(array)
    

if __name__=="__main__":
    run_tests()
        


