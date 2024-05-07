# rotate image to 90 degree

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

n = len(mat)
print((n+1)//2)

for i in range((n+1)//2):
    for j in range(n//2):
        temp = mat[n-j-1][i]
        mat[n - j - 1][i] = mat[n-1-i][n-1-j]
        mat[n - 1 - i][n - 1 - j] = mat[j][n-1-i]
        mat[j][n - 1 - i] = mat[i][j]
        mat[i][j] = temp
        print(temp)
print(mat)