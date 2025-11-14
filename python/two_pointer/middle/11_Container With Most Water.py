"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    low = 0
    high = len(height) - 1

    max_water = 0

    while low <= high:
        current_water = min(height[low], height[high]) * (high - low)

        if current_water > max_water:
            max_water = current_water

        if height[low] < height[high]:
            low += 1
        else:
             high -= 1

    return max_water

print(maxArea([1, 1]))