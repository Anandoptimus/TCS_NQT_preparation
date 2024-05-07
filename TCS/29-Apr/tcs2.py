# word search

board = [['A', 'B', 'C', 'E'],
         ['S', 'F', 'C', 'S'],
         ['A', 'D', 'E', 'E']]
path = set()
word = 'ABCCED'
row, col = len(board), len(board[0])


def dfs(r, c, i):
    if i == len(word): return True

    elif r<0 or c<0 or r>= row or c>= col or word[i] != board[r][c] or ((r, c) in path): return False

    path.add((r,c))
    res = (dfs(r+1, c, i+1) or
           dfs(r-1, c, i+1) or
           dfs(r, c+1, i+1) or
           dfs(r, c-1, i+1))

    path.remove((r, c))
    return res


for r in range(len(board)):
    for c in range(len(board[0])):
        if dfs(r, c, 0):
            print(True)
# print(False)