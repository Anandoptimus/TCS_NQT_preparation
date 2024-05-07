a = [16, 4, 23, 8, 15, 42, 1, 2]
k = 19
a.sort()
print(a)
start = 0
end = len(a)-1
m = []
while start < end:
    if a[start] + a[end] == k:
        print(start, end)
        m.append(start)
        m.append(end)
        break
    elif a[start] + a[end] > k:
        end -= 1
    elif a[start] + a[end] < k:
        start += 1


print(m)