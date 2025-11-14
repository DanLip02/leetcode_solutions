"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    low = 0
    high = len(numbers) - 1
    while low <= high:
        if numbers[low] + numbers[high] == target:
            return [low + 1, high + 1]
        elif numbers[low] + numbers[high] < target:
            low += 1
        else:
            high -= 1
    return None

print(twoSum([2,3,4], 6))