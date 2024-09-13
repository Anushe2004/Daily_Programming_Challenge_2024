import numpy as np # type: ignore

def find_leaders(array, n):
    leaders = []  
    max_from_right = array[-1]  
    leaders.append(max_from_right)

    
    for i in range(n-2, -1, -1):
        if array[i] > max_from_right:
            leaders.append(array[i])
            max_from_right = array[i]

    
    return leaders[::-1]


array = [1, 2, 3, 4, 0]
print(find_leaders(array, len(array)))  

array_1 = [7, 10, 4, 10, 6, 5, 2]
print(find_leaders(array_1, len(array_1)))  

array_2 = [5]
print(find_leaders(array_2, len(array_2)))  

array_3 = [100, 50, 20, 10]
print(find_leaders(array_3, len(array_3)))  

array_4 = np.arange(1000001)
print(find_leaders(array_4, len(array_4)))  
