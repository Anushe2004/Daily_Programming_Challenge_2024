def Findmaxwater(height):
    left = 0
    n = len(height)
    right = n - 1
    left_max = 0
    right_max = 0
    amount_of_water = 0
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                amount_of_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                amount_of_water += right_max - height[right]
            right -= 1
    return amount_of_water

height =  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Findmaxwater(height))

heights = [4, 2, 0, 3, 2, 5]
print(Findmaxwater(heights))

height_1 =  [1, 1, 1]
print(Findmaxwater(height_1))

height_2 = [5]
print(Findmaxwater(height_2))

height_3 = [2, 0, 2]
print(Findmaxwater(height_3))