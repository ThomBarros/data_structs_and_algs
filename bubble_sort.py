
def bubble_sort(array):
    n = len(array)
    while not (n <= 1):
        new_n = 0
        for i in range(1, n):
            if array[i - 1] > array[i]:
                temp = array[i - 1]
                array[i - 1] = array[i]
                array[i] = temp
                new_n = i
        n = new_n

def run_tests():
    array = [2, 5, 4, 1, 7, 9, 8, 3, 6]
    print(array)
    bubble_sort(array)
    print(array)


if __name__=="__main__":
    run_tests()

