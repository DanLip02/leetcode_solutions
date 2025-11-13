def searchRange(nums, target):
    def findLeft(nums, target):
        low, high = 0, len(nums) - 1
        left = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                if nums[mid] == target:
                    left = mid
                high = mid - 1
        return left

    def findRight(nums, target):
        low, high = 0, len(nums) - 1
        right = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            else:
                if nums[mid] == target:
                    right = mid
                low = mid + 1
        return right

    left = findLeft(nums, target)
    right = findRight(nums, target)
    return [left, right]


""" or can be"""
def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    left = low

    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
    right = high

    if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
        return [left, right]
    return [-1, -1]