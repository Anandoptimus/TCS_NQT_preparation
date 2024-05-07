# a = [1, 3, 4, 5, 9]
a = [1, 2, 3, 4]
k = 2
l = 0
r = len(a)
while l < r:
    mid = (l + r) // 2
    if a[mid] - mid - 1 < k:
        l = mid+1
    else:
        r = mid

print(l+k)