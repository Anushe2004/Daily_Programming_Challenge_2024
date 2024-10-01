def first_k_times(array, k):
    for i in array:
        count = 0
        for j in array:
            if i==j:
                count += 1
        if count == k:
            return i
    return -1
arr = [2, 3, 4, 2, 2, 5, 5]
k = 2
print(first_k_times(arr, 2))

arr_1 = [1, 1, 1, 1]
k = 1
print(first_k_times(arr_1, 1))

array = [10]
k = 1
print(first_k_times(array, 1))

arr_2 = [6, 6, 6, 6, 7, 7, 8, 8, 8]
k = 3
print(first_k_times(arr_2, 3))

