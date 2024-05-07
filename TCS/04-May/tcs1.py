# 90 rotate matrix
mat = [[5, 1, 9, 11],
       [2, 4, 8, 10],
       [13, 3, 6, 7],
       [15, 14, 12, 16]]

l, r = 0, len(mat) - 1

while l < r:
    for i in range(r - l):
        top, bottom = l, r
        topleft = mat[top][l+i]
        mat[top][l+i] = mat[bottom-i][l]
        mat[bottom-i][l] = mat[bottom][r-i]
        mat[bottom][r-i] = mat[top+i][r]
        mat[top+i][r] = topleft
    l += 1
    r -= 1

print(*mat, sep='\n')