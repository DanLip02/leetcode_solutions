"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""


def isMonotonic(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    left = 0
    increase = False
    decrease = False
    for right in range(1, len(nums)):
        if nums[left] <= nums[right]:
            left += 1
            increase = True
        else:
            increase = False
            break
    left = 0
    for right in range(1, len(nums)):
        if nums[left] >= nums[right]:
            left += 1
            decrease = True
        else:
            decrease = False
            break

    print(decrease, increase)
    if decrease == True or increase == True:
        return True
    else:
        return False

print(isMonotonic([6, 5, 4, 4]))

#################
def isMonotonic(nums):
    inc = True   # предполагаем, что массив не убывает
    dec = True   # предполагаем, что массив не возрастает

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            dec = False
        if nums[i] < nums[i-1]:
            inc = False

    return inc or dec
