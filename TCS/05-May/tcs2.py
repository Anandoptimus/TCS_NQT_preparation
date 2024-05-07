# maximum subarray

a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

curnum = 0
res = a[0]
for i in a:
    if curnum < 0:
        curnum = 0
    curnum += i
    res = max(curnum, res)

print(res)
