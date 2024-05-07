# subsets
ans = []
num = [1, 2, 3]
n = 3


def helper(op, start_index):
    if start_index == n:
        ans.append(list(op))
        return

    op.append(num[start_index])
    helper(op, start_index+1)

    # excluded
    op.pop()
    helper(op, start_index+1)


helper([], 0)
print(ans)


