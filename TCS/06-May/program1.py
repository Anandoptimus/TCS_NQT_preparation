# tcs exam complete with 4/7 test case for the first code and 7/7 test case for the second code

# a = [3, 3, 3, 2, 2, 1, 1, 1]
a = [1]
op = 3, 1

# a = list(map(int, input().split()))

cons = (len(a) // 3) + 1
print(cons)
dic = {}
if len(a) < 2:
    print([])
else:
    for i in a:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    print(dic)
    res = []
    for i, j in dic.items():
        if j == cons:
            res.append(i)

    for i in res:
        print(i, end=' ')


# second problem
a = [5, 6, 7, 5, 6, 7, 5, 6, 7]
n = 9


def sort_it(a):
    a.sort()


sort_it(a)
for i in a:
    print(i, end=' ')
