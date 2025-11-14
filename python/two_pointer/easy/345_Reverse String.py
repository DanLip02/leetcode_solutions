"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

"""


def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """

    low = 0
    high = len(s) - 1

    while low < high:
        s[low], s[high] = s[high], s[low]

        low += 1
        high -= 1

    return s

print(reverseString(["o", "b"]))
