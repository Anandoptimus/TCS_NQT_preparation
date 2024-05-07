a = [5, 5, 10, 100, 10, 5]

cur = a[0]
per = a[0]
for i in range(1, len(a)):
    cur = max(cur, a[i]+cur)
    per = max(cur, per)
print(per)


print(5&10)