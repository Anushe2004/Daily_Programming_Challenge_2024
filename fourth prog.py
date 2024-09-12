def merge_two_arrays(arr_1, arr_2):
    res_arr = sorted(arr_1 + arr_2)
    m = len(arr_1)
    arr_1 = res_arr[:m]
    arr_2 = res_arr[m:]
    return arr_1, arr_2

arr_1 = [1, 3, 5]
arr_2 = [2, 4, 6]
print(merge_two_arrays(arr_1, arr_2))
