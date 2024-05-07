# color problem
# a = [1, 1, 0, 2, 0, 2]
a = [2, 0, 1]
dic = {}
# dic.va
for i in range(len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)