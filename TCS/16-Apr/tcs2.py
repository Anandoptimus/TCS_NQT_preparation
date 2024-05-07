n = 1
# 7
a = 0
b = 1
sum = 0
if n == 0:
    sum = 1

for i in range(n):
    c = a + b
    sum += a
    a = b
    b = c

print(sum)
