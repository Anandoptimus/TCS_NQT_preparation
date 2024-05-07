# vaild suduko
import collections

board = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0]
]

col = collections.defaultdict(set)
row = collections.defaultdict(set)
square = collections.defaultdict(set)

for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            continue
        elif board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]:
            print('False')

        col[c].add(board[r][c])
        row[r].add(board[r][c])
        square[(r//3, c//3)].add(board[r][c])


print('True its valid suduko')
