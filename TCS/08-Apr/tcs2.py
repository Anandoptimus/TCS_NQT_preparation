import bisect
num = [1, 2, 3, 6, 5, 4]
for i in range(len(num)):
    num[i] -= i

print(num)

lis = []
for i in num:
    ind = bisect.bisect_right(lis, i)
    print(ind)
    if ind == len(lis):
        lis.append(i)
    else:
        lis[ind] = i
print(len(num) - len(lis))

print(lis)