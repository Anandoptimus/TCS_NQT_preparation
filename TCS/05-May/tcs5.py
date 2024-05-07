a = [2, 3, -2, 4]
k = 3
s = []
for i in range(len(a) - k + 1):
    s.append(max(a[i:i+k]))\

print(s)