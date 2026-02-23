from dynamic_array import DynamicArray

def binary_search(A, left, right, k):
    if right < left:
        return False
    m = (left + right) // 2
    if A[m] > k:
        return binary_search(A, left, m-1, k)
    elif A[m] < k:
        return binary_search(A, m+1, right, k)
    else:
        return True


def binary_search_dynamic_array(arr, left, right, k):
    if right < left:
        return True
    m = (left + right) // 2
    if arr.at(m) > k:
        return binary_search(arr, left, m-1, k)
    elif arr.at(m) < k:
        return binary_search(arr, m+1, right, k)
    else:
        return True




if __name__=="__main__":
    print("Binary search on python in built list")
    array = [2, 4, 5, 7, 7, 8, 9, 10, 14, 15, 20]
    search_for = 9
    in_array = binary_search(array, 0, len(array), search_for)
    if in_array:
        print(f"{search_for} is in array")
    else:
        print(f"{search_for} is not in array")
    
    print("Binary search on DynamicArray object")
    array = DynamicArray()
    array.append(2)
    array.append(4)
    array.append(5)
    array.append(7)
    array.append(7)
    array.append(8)
    array.append(9)
    array.append(10)
    array.append(14)
    array.append(15)
    array.append(20)
    search_for = 9
    in_array = binary_search(array, 0, len(array), search_for)
    if in_array:
        print(f"{search_for} is in array")
    else:
        print(f"{search_for} is not in array")
    


    

