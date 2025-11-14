"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""

import random

# Параметры большого массива
n = 100_000

# Случайные числа от 1 до n-2
nums = list(range(1, n-1))

# Вставим два максимума не по краям
max1 = n
max2 = n-1

# Вставляем примерно в середину массива
nums.insert(n//3, max1)
nums.insert(2*n//3, max2)

# Перемешаем небольшие элементы, чтобы не упорядочить полностью
random.shuffle(nums[:n//3])
random.shuffle(nums[n//3+1:2*n//3])
random.shuffle(nums[2*n//3+1:])

# Проверим первые 20 элементов для визуального контроля


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low = 0
    high = len(nums) - 1
    max_im = 0
    while low < high:
        current_im = (nums[low] - 1) * (nums[high] - 1)

        if current_im > max_im:
            max_im = current_im
        if nums[low] < nums[high]:
            low += 1
        else:
            high -= 1

    return max_im

print(maxProduct(nums))


####################### another solution


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max1 = max2 = 0

    for x in nums:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x

    return (max1 - 1) * (max2 - 1)

print(maxProduct([1,1,1,1,1,5,5,5,5,5]))