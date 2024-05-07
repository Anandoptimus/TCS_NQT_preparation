col = 4
row = 4
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
s = []
print(a)
row_b = 0
col_b = 0
while row_b<=row and col_b <= col:
# traverse right
    for i in range(col_b, col):
        print(a[row_b][i])
        s.append(a[row_b][i])

    row_b += 1

    for i in range(row_b, row):
        print(a[i][col-1])
        s.append(a[i][col-1])
    col -= 1

    if row_b <= row:
        for i in range(col-1, col_b-1, -1):
            print(a[row-1][i])
            s.append(a[row-1][i])
    row -= 1

    if col_b <= col:
        for i in range(row-1, row_b-1, -1):
            print(a[i][col_b])
            s.append(a[i][col_b])
    col_b += 1

print(s)