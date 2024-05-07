n = 8
m = 4
a1 = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]
a2 = [1 ,2 ,3 ,1]
count  = 0
for i in range(m):
    if a2[i] in a1:
        a1.remove(a2[i])
        count += 1

print(m , count)

if count == m:
    print('correct')