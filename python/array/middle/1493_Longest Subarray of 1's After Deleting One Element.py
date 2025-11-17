"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""


def longestSubarray(nums):
    left = 0
    count_zero = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            count_zero += 1

        while count_zero > 1:
            if nums[left] == 0:
                count_zero -= 1
            left += 1

        max_len = max(max_len, right - left)

    return max_len

print(longestSubarray([0,1,1,1,0,1,1,0,1]))


