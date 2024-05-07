# subarray with given sum
a = [1, 4, 20, 3, 10, 5]
n = 6
k = 33
left = 0
right = 0
cur = 0
count = []
cut = []
while left <= n or right <= n:
    if cur == k:
        val = [i for i in count if i not in cut]
        print(val)
        break
    if cur < k:
        cur += a[right]
        count.append(a[right])
        right += 1
        # print(count)
    elif cur > k:
        cur -= a[left]
        cut.append(a[left])
        # print(cut)
        left += 1


