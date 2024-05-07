def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 1
    else:
        return 0


lis = []
a = 0
b = 1
for i in range(a, b+1):
    a = prime(i)
    if a == 0:
        lis.append(i)
print(lis)
