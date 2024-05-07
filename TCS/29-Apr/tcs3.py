# N Queen
n = 4
col = set()
posdig = set()
negdig = set()

res = 0


def backtracking(r):
    if r == n:
        global res
        res += 1
        return
    for c in range(n):
        if c in col or (r+c) in posdig or (r-c) in negdig:
            continue

        col.add(c)
        posdig.add(r+c)
        negdig.add(r-c)
        backtracking(r+1)
        col.remove(c)
        posdig.remove(r+c)
        negdig.remove(r-c)

backtracking(0)
print(res)
