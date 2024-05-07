n = 6
a = [2, 3, 5, 6, 8, 10]
k = 10
count = 0
cu = 0
for i in range(n):
    cur = i
    for j in range(i+1, n):
        if cur == k:
            print(cur)
            count += 1
        cur += j
        print(cur)

print(count)