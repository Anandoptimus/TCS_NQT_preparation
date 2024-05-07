from pprint import pprint
mat = [[1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4],
       [1, 2, 3, 4]]

print(len(mat))

for i in range(len(mat)):
       for j in range(len(mat)):
              if (i==0 and j >0) or (i ==1 and j >1) or (i ==2 and j >2):
                     mat[i][j] = 0

pprint(mat)