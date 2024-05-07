n = 4
res = []
board = [["."]*n for i in range(n)]
print(board)
col = set()
posDig = set()
negDig = set()


def bfs(r):
    if r == n:      # end of the row
        copy = [''.join(row) for row in board]
        res.append(copy)
        return res

    for c in range(n):
        if c in col or (r+c) in posDig or (r-c) in negDig:
            continue

        col.add(c)
        posDig.add(r+c)
        negDig.add(r-c)
        board[r][c] = 'Q'
        bfs(r+1)
        col.remove(c)
        posDig.remove(r+c)
        negDig.remove(r-c)
        board[r][c] = '.'


bfs(0)
print(res)
