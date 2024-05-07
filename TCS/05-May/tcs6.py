# maximum subarray product
num = [2, 3, -2, 4]

res = max(num)
curmin, curmax = 1, 1

for n in num:
    tmp = n * curmax
    curmax = max(n * curmax, n * curmin, n)
    curmin = min(tmp, n * curmin, n)
    res = max(res, curmax)

print(res)