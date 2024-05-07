# spiral matrix
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
res = []
def spiral(m):
    left, right = 0, len(m[0])
    top, bottom = 0, len(m)
    print(left, right, top, bottom)
    # print(res)
    while left <= right and top <= bottom:
        for i in range(left, right):
            res.append(m[top][i])
        top += 1

        for i in range(top, bottom):
            res.append(m[i][right-1])
        right -= 1
        print(res)

        if not (left < right and top < bottom):
            break

        for i in range(right-1, left-1, -1):
            res.append(m[bottom-1][i])
        bottom -= 1

        for i in range(bottom-1, top-1, -1):
            res.append(m[i][left])
        left += 1

    return res

print(spiral(matrix))
