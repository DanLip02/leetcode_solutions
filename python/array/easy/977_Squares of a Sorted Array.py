"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    def quicksort(arr):
        if len(arr) < 2:
            return arr

        else:
            pivot = arr[0]
            less = [i for i in arr[1:] if i <= pivot]
            greater = [i for i in arr[1:] if i > pivot]
            return quicksort(less) + [pivot] + quicksort(greater)

    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    return sorted(nums)

print(sortedSquares([-4,-1,0,3,10]))


########## another solution
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n

    left, right = 0, n - 1
    pos = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] * nums[left]
            left += 1
        else:
            result[pos] = nums[right] * nums[right]
            right -= 1
        pos -= 1

    return result