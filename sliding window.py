def max_sub_array(array, N, k):
    result = []
    for i in range(N - k + 1):
        res = array[i]
        for j in range(1, k):
            if array[i + j] > res:
                res = array[i + j]
        result.append(res)
    return result

array = [1, 5, 3, 2, 4, 6]
k = 3
N = len(array)
result = max_sub_array(array, N, k)
print(result)

array_1 = [1, 2, 3, 4]
k = 2
n = len(array_1)
result_1 = max_sub_array(array, n, k)
print(result_1)


array_2 =  [7, 7, 7, 7]
k = 1
m = len(array_2)
result_2 = max_sub_array(array_2, m, k)
print(result_2)