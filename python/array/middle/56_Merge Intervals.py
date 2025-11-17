"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

"""


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # если это первый или нет пересечения
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # пересечение — расширяем
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

#####################
def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out