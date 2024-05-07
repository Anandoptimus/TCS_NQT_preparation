nums = [3, 4, -7, 1, 3, 3, 1, 4]
sum = 7
n = len(nums)


b = []
for i in range(n):
    cur = 0
    a = []
    for j in range(i, n):
        # print(j)
        cur += nums[j]
        a.append(nums[j])
        if cur == sum:
            b.append(list(a))

        # print(j)
print(b)
