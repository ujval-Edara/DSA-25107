def linear_search(arr, target):
    # av.sc.u4cse25107
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_array = [10, 23, 45, 70, 11, 15]
target_val = 70
print(linear_search(my_array, target_val))