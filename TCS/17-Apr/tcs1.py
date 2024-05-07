n = 3
a = [1, 2, 2]
print("()")
for i in range(n):
    for j in range(i, n):
        ne = []
        for k in range(i, j+1):
            ne.append((a[k]))
            print(f'({a[k]})', end='')
            print(ne)
        print()

