a = 'dnxeuoqqeklaitgdphcspij'
n = 5
res = ''
increment = 2 * (n-1)
if n == 1:
    print('stop')
else:
    for r in range(n):
        increment = 2 * (n-1)
        # print(r, len(a), increment)
        for i in range(r, len(a), increment):
            res += a[i]
            print(res)
            if (r > 0 and r < n-1 and i + increment - 2 * r < len(a)):
                res += a[i + increment - 2*r]
                print()
                print(1, res)

print(res == "depnqkdhxqlgcjeoatsiuip")