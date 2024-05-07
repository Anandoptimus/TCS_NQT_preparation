# binary list ..find the max consecutive sum with almost of k zeros

a = [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1]

zerocount = 0
start = 0
maxnum = 0
k = 3

for end in range(len(a)):
    if a[end] == 0:
        zerocount += 1

    while zerocount > k:
        if a[start] == 0:
            zerocount -= 1
        start += 1

    maxnum = max(maxnum, end - start + 1)


print(maxnum)

dic = {1:3, 1:2}
print(dic)