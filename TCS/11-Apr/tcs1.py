a = [1, 2, 2, 4]

i = 0
for j in range(1, len(a)):
    if a[i] != a[j]:
        i += 1
        a[i] = a[j]

print(i)
print(a)