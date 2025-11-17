"""
You are given a binary string s consisting only of zeroes and ones.

A substring of s is considered balanced if all zeroes are before ones and the number of zeroes is equal to the number of ones inside the substring. Notice that the empty substring is considered a balanced substring.

Return the length of the longest balanced substring of s.

A substring is a contiguous sequence of characters within a string.
"""


def findTheLongestBalancedSubstring(s):
    i = 0
    n = len(s)
    best = 0

    while i < n:
        zeros = 0
        while i < n and s[i] == "0":
            zeros += 1
            i += 1

        ones = 0
        while i < n and s[i] == "1":
            ones += 1
            i += 1

        best = max(best, 2 * min(zeros, ones))

    return best

print(findTheLongestBalancedSubstring("011"))
