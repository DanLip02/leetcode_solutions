"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""


def climbStairs(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 1

    return self.climbStairs(n - 1) + self.climbStairs(n - 2)

"""
or it can be
"""


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 2:
        return 1
    a = 1
    b = 2
    for _ in range(3, n + 1):
        a,b = b, a + b
    return b

print(climbStairs(10))