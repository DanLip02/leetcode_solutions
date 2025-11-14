"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

"""

def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict_ = {}
    for num in nums:
        if num not in dict_:
            dict_[num] = 1
        else:
            dict_[num] += 1

    for key, value in dict_.items():
        if value == 1:
            return key

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))


def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            high = mid
    return nums[low]

print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))