# three sum
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0]
num = sorted(nums)
print(num)
res = []
ans = []
for i in range(len(nums)):
    a = num[i]
    left = i+1
    right = len(nums)-1
    while left < right:
        if a + num[left] + num[right] > 0:
            right -= 1
        elif a + num[left] + num[right] < 0:
            left += 1
        else:
            res.append([a, num[left], num[right]])
            left += 1
            right -= 1
            # print(res)
print(res)
for i in res:
    if i not in ans:
        ans.append(i)

print(ans)