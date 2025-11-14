"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """

    res = []
    if not nums:
        return res

    start = nums[0]
    end = nums[0]

    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + '->' + str(end))

            start = num
            end = num

    if start == end:
        res.append(str(start))
    else:
        res.append(str(start) + '->' + str(end))

    return res

print(summaryRanges([0,1,2,4,5,7]))
