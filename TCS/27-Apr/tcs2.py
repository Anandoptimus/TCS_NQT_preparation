a, b = map(int, input().split())
n = 3
cur = 0
for i in range(a, b+1):
    print(i)
    cur += i**n

print(cur)