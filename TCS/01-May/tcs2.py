# word search 2
board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]],
words = ["oath","pea","eat","rain"]
# Output = ["eat","oath"]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

    def add(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isword = True


class solution:
    def findword(self, board, words):
        root = TrieNode()
        for c in words:
            root.add(c)
        row, col = len(board), len(board[0])
        visit, res = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == row or c == col or board[r][c] not in node.children or (r, c) in visit):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isword:
                res.add(word)

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r, c))

        for r in range(row):
            for c in range(col):
                dfs(r, c, root, "")

        return list(res)


a = solution()
op = a.findword(board, words)
print(op)
