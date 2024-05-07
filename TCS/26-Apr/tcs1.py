a = [3, 4, -7, 1, 3, 3, 1, 4]
n = len(a)
k = 7
ans = []


def helper(op, start):
    if start == n:
        ans.append(list(op))
        return
    op.append(a[start])
    helper(op, start+1)
    op.pop()
    helper(op, start+1)

helper([], 0)
count = []
# print(ans)
for i in ans:
    if sum(i) == k:
        count.append(i)

print(count)