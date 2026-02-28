
def insertion_sort(array):
    i = 1
    while i < len(array):
        x = array[i]
        j = i
        while j > 0 and array[j - 1] > x:
            array[j] = array[j - 1]
            j -= 1
        array[j] = x
        i += 1

def run_tests():
    array = [2, 9, 1, 7, 8, 5, 4, 6, 3]
    print(array)
    insertion_sort(array)
    print(array)


if __name__=="__main__":
    run_tests()
