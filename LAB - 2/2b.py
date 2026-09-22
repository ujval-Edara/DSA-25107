def binary_search_sorted(arr, target):
    # aav.sc.u4cse25107
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

sorted_array = [11, 22, 34, 45, 55, 67, 89]
target_val = 45
print(binary_search_sorted(sorted_array, target_val))