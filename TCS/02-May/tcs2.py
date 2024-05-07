# a = [-1, 0, 1, 2, -1, -4]
a = [-1, 2, 1, -4]
tar = 1
a = sorted(a)
# /print(a)
mini = len(a)
res = 0
for i in range(len(a)-2):
    cur = a[i]
    l = i+1
    r = len(a) - 1
    while l < r:
        summ = cur + a[l] + a[r]
        # print(summ)
        if summ == tar:
            break
        elif summ > tar:
            r -= 1
        else:
            l += 1

        difftar = abs(summ - tar)
        if difftar < mini:
            # print(summ)
            res = summ
            mini = difftar

print(res)


