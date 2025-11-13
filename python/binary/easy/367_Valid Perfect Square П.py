def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 2:
        return True

    low = 0
    high = num - 1
    while low <= high:
        mid = (low + high) // 2
        root = mid * mid
        if root == num:
            return True
        elif root < num:
            low = mid + 1
        else:
            high = mid - 1

    return False

print(isPerfectSquare(256))