def find_duplicates(array):
    m = len(array)
    m = n + 1
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return array[i]
    return -1

array = [3, 1, 3, 4, 2]
n = 4
print(find_duplicates(array))