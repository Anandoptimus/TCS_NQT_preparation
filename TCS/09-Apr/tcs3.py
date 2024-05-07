# Input: samples[] = {345, 604, 321, 433, 704, 470, 808, 718, 517, 811}, ranges[] = {{300, 380}, {400, 700}}
# Output: 2 4

sample = [345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
ran = [[300, 380], [400, 700]]


a = []
for i in range(len(ran)):
    c = 0
    l, h = ran[i][0], ran[i][1]
    for val in sample:
        if l <= val <= h:
            c += 1
    a.append(c)

print(a)



# print(count, count1)
