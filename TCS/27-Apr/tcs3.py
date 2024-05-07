from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
a = [1, 2, 3]

m = permutations(a)
d = combinations_with_replacement(a, 2
                                  )
z = []
z1 = []
for i in m:
    z.append(list(i))

for i in d:
    z1.append(i)

print(z1)
print(z)