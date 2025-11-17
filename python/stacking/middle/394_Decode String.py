"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.
"""


def decodeString(s):
    """
    :type s: str
    :rtype: str
    """

    stack_nums = []
    stack_strs = []
    current_str = ""
    current_num = 0

    for ch in s:
        if ch.isdigit():
            current_num = current_num * 10 + int(ch)

        elif ch == "[":
            stack_nums.append(current_num)
            stack_strs.append(current_str)
            current_num = 0
            current_str = ""

        elif ch == "]":
            k = stack_nums.pop()
            prev_str = stack_strs.pop()
            current_str = prev_str + current_str * k

        else:  # letter
            current_str += ch

    return current_str