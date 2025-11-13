def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        guess = isBadVersion(mid)
        if guess is False:
            low = mid + 1
        else:
            high = mid - 1

    return low

#### correct one

def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        guess = isBadVersion(mid)
        if guess is False:
            low = mid + 1
        else:
            high = mid - 1

    return low