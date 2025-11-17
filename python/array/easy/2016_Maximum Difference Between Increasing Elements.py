"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""


def maximumDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_so_far = nums[0]
    max_diff = -1

    # Step 2 : Apply Logic and Loop
    for i in range(1, len(nums)):
        if nums[i] > min_so_far:
            max_diff = max(max_diff, nums[i] - min_so_far)
        else:
            min_so_far = nums[i]

    # Step 3 : Return the Result
    return max_diff


#############

def maximumDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    min_price = float('inf')
    max_profit = 0

    for p in nums:

        if p < min_price:
            min_price = p

        profit = p - min_price
        if profit > max_profit:
            max_profit = profit

    if max_profit == 0:
        return -1
    else:
        return max_profit