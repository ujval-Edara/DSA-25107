def binary_search_unsorted(arr, target):
    # av.sc.u4cse25107
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

unsorted_array = [67, 11, 89, 22, 55, 45, 34]
target_val = 45
print(binary_search_unsorted(unsorted_array, target_val))