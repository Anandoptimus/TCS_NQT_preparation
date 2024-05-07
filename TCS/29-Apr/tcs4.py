a = [1, 1, 1, 0, 1, 1, 0, 1, 1]
m = 0
ans = 0
for i in range(len(a)):
    if a[i] == 1:
        m += a[i]
        ans = max(ans, m)
    elif a[i] == 0:
        m = 0
print(ans)
