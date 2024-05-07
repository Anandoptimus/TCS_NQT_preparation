n = [1, 2, 3]
a = 3
ans = []

def helper(op, start_index):
    if start_index == a:
        ans.append(list(op))
        return

    op.append(n[start_index])
    helper(op, start_index+1)

    op.pop()
    helper(op, start_index+1)

helper([], 0)

print(ans)

