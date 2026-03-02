
def selection_sort(array):
    smallest = array[0] 

    for i in range(0, len(array)):
        smallest = i

        for j in range(i, len(array)):
            if array[j] < array[smallest]:
                smallest = j

        if not smallest == i:
            temp = array[i]
            array[i] = array[smallest]
            array[smallest] = temp


def run_tests():
    array = [2, 9, 1, 7, 5, 4, 6, 3, 8]
    print(array)
    selection_sort(array)
    print(array)


if __name__=="__main__":
    run_tests()


