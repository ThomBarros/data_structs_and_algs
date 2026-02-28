def merge_sort(array):
    if len(array) <= 1:
        return array

    left = []
    right = []

    for i in range(len(array)):
        if i < (len(array) // 2):
            left.append(array[i])
        else:
            right.append(array[i])
       
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while not (len(left) == 0) and not (len(right) == 0):
        if left[0] <= right[0]:
            result.append(left[0])
            del left[0]
        else:
            result.append(right[0])
            del right[0]

    while not len(left) == 0:
        result.append(left[0])
        del left[0]
    while not len(right) == 0:
        result.append(right[0])
        del right[0]

    return result


def run_tests():
    arr = [101, 6, 2, 79, 4, 25, 0, 6, 8, 1, 350, 3, 15, 5, 11, 7]
    sorted_arr = merge_sort(arr)
    print(arr)
    print(sorted_arr) 


if __name__=="__main__":
    run_tests()

