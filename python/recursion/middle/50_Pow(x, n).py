"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    if n == 0:
        return 1

    if n < 0:
        return 1 / myPow(x, -n)

    half = myPow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * x

print(myPow(2, -200000000))