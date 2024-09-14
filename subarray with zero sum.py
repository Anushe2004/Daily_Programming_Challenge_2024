def findzeroSubarraysum(array):
    n = len(array)
    dict = {}
    result = []
    res = 0
    for i in range(n):
        res += array[i]
        
        
        if res == 0:
            result.append((0, i))

        if res in dict:
            for start in dict[res]:
                result.append((start + 1, i - 1))
        if res in dict:
            dict[res].append(i)
        else:
            dict[res] = [i]

    return result
    
array = [4, -1, -3, 1, 2, -1]
print(findzeroSubarraysum(array))

array_1 = [1, 2, 3, 4]
print(findzeroSubarraysum(array_1))

array_2 = [0, 0, 0]
print(findzeroSubarraysum(array_2))

array_3 = [-3, 1, 2, -3, 4, 0]
print(findzeroSubarraysum(array_3))

array_4 = [1, -1, 2, -2, 3, -3] * 10000
print(findzeroSubarraysum(array_4))

