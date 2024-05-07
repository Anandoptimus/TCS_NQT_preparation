a = [1, 2, 3, 4, 5]
d = 2
d%=len(a)
a[:] = a[-d:] + a[:-d]
print(a)

s = [1, 2, 3, 4, 5]
d = 2

d%=len(s)
s[:] = s[d:] + s[:d]
print(s)