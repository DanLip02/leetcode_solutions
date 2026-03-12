
def takeCharacters(self, s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    from collections import Counter
    n = len(s)
    total = Counter(s)
    if min(total[c] for c in 'abc') < k:
        return -1

    max_window_len = 0
    counter = Counter()
    left = 0
    for right in range(n):
        counter[s[right]] += 1
        while left <= right and any(total[c] - counter[c] < k for c in 'abc'):
            counter[s[left]] -= 1
            left += 1
        max_window_len = max(max_window_len, right - left + 1)

    return n - max_window_len

