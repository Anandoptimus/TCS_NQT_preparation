from pprint import pprint
a = [[1, 2, 3, 0],
     [0, 2, 4, 6],
     [1, 2, 3, 5]]

firstrow = False
firstcol = False

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 0:
            if  i == 0:
                firstrow = True
            elif j == 0:
                firstcol = True
            a[0][j] = 0
            a[i][0] = 0

for i in range(1, len(a)):
    for j in range(1, len(a[0])):
        if a[i][0] == 0 or a[0][j] == 0:
            a[i][j] = 0

if firstcol:
    for i in range(len(a[0])):
        a[0][i] = 0

if firstrow:
    for i in range(len(a)):
        a[i][0] = 0


pprint(a)
