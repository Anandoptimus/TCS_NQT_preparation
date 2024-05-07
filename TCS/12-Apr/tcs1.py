from collections import OrderedDict
od = OrderedDict()

a = [1, 2, 3, 2, 1]
for i in a:
    if i not in od:
        od[i] = 1
    else:
        od[i] += 1

n = []
for i in od:
    print(i)
    n.append(i)

print(n)