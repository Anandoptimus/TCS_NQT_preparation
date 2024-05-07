s = "123"
target = 6
res = []


def dfs(i, path, cur_num, prenum):
    if i >= len(s):
        if cur_num == target:
            res.append(path)
        return

    for j in range(i, len(s)):
        if j > i or s[i] == '0':
            break
        num = int(s[i:j+1])
        if i == 0:
            dfs(j+1, path+str(num), cur_num+num, num)
        else:
            dfs(j+1, path + "+" + str(num), cur_num + num, num)
            dfs(j+1, path + '-' + str(num), cur_num - num, -num)
            dfs(j+1, path + '*' + str(num), cur_num - prenum + prenum * num, prenum * num)
#                                           1+2+3+4 + (-4) + (4 * 5) bcz of priority operator


dfs(0, "", 0, 0)
print(res)
