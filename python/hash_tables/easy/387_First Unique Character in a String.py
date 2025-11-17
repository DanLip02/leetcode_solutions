"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 2:
        return 0

    dict_ = {}
    for ch in s:
        if ch not in dict_:
            dict_[ch] = 1
        else:
            dict_[ch] += 1

    for i, ch in enumerate(s):
        if dict_[ch] == 1:
            return i
    return - 1
