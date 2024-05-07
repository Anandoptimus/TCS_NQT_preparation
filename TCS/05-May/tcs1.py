a = [1, 2, 3, 4, 8, 9]
ans = []
n = len(a)


def helper(op, start_ind):
    if start_ind == n:
        ans.append(list(op))
        return

    op.append(a[start_ind])
    helper(op, start_ind+1)
    op.pop()
    helper(op, start_ind+1)


helper([], 0)

check = []
# print(ans)
for i in ans:
    print(len(i))
    if len(i) == 3:
        if i not in check:
            print('hi')
            check.append(list(i))
    # if len(i) == 3:
    #     # if i not in check:
    #     ans.append(i)

print(check)
