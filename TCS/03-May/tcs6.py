a = [2, 3, 1, 1, 4]


def jump(a):
    l = r = 0
    res = 0

    while r < len(a)-1:
        farest = 0
        for i in range(l, r+1):
            farest = max(farest, i + a[i])
        l = r+1
        r = farest
        res += 1
    return res

print(jump(a))
