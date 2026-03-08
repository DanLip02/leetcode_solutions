def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    left = 0
    used = {}
    max_len = 0

    for right in range(len(s)):
        char = s[right]

        # Если символ уже в окне и находится не левее текущего left
        if char in used and used[char] >= left:
            left = used[char] + 1

        used[char] = right
        max_len = max(max_len, right - left + 1)

    return max_len