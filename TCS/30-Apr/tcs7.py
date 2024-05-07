# colored
nums = [3, 3, 4]
dic = {}
for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

print(dic)
max_val = max(dic.values())
for i, j in dic.items():
    if j == max_val:
        print(i)
