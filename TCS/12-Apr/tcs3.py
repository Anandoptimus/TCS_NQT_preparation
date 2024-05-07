arr = [5, 10, 15]
ans = 0
for i in range(32):
    c = 0


    for j in arr:
        # print((j >> i)&1)
        if (j >> i) & 1:
            c += 1

    print(c)

    if c > 1:
        ans += (2 ** i) * ((c - 1) * c) // 2
        print(ans)
print(ans)