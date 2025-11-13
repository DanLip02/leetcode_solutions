"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array

"""


def findKthPositive(arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        missed = arr[mid] - (mid + 1)
        if missed < k:
            low = mid + 1
        else:
            high = mid - 1

    return low + k