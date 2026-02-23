
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


if __name__=="__main__":
    array = [2, 4, 5, 7, 7, 8, 9, 10, 14, 15, 20]
    search_for = 9
    in_array = binary_search(array, 0, len(array), search_for)
    if in_array:
        print(f"{search_for} is in array")
    else:
        print(f"{search_for} is not in array")


