# permutation using backtracking

def perum(ind, a, ans):
    if ind == len(a):
        b = []
        for i in a:
            b.append(i)

        ans.append(b)
        return

    for i in range(ind, len(a)):
        swap(i, ind, a)
        perum(ind+1, a, ans)
        swap(i, ind, a)


def swap(a, b, num):
    temp = num[a]
    num[a] = num[b]
    num[b] = temp


# a = ['A', 'B', 'C']
a = [1, 2, 3]

ans = []
perum(0, a, ans)
print(ans)
