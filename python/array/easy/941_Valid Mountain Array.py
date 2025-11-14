"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
"""

def validMountainArray(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    n = len(arr)
    if len(arr) < 3:
        return False

    left = 0
    right = n - 1

    while left + 1 < n and arr[left] < arr[left + 1]:
        left += 1

    while right - 1 >= 0 and arr[right] < arr[right - 1]:
        right -= 1

    return left == right and 0 < left < n - 1


print(validMountainArray([0,3,5, 6, 2, 1]))