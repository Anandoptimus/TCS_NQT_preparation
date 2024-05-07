# bit manipulation

n = int('000000001011')

res = 0
while n:
    n = n & (n-1)
    res += 1
    print(res)
    # res += n % 2
    # n = n >> 1
print(res)