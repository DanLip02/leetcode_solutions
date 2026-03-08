
nums = [1, 2, 3, 4, 10, 11, 12, 13, 14]
check = [x for x in range(1, len(nums) + 1)]
seen = set(nums)
res = []
for num in check:
    if num not in seen:
        res.append(num)

print(res)