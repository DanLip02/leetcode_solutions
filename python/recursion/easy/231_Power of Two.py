"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

"""


def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    print(n)
    if n <= 0:
        return False

    if 0 < n < 2:
        return True

    if n % 2 == 0:
        return isPowerOfTwo(n // 2)
    else:
        return False

print(isPowerOfTwo(32))


"""
or can be return n > 0 and (n & (n - 1)) == 0
"""