from itertools import permutations, combinations, product

a= 'BD'
per = permutations(a)
pro = product(a, repeat=len(a))
# com = combinations(a)
print(per)
b = []
for i in pro:
    b.append(''.join(i))

for i in b:
    print(i, end=' ')
# for i in com:
#     print(i)
# for i in per:
#     b.append(''.join(i))
#     print(i)

print(b)