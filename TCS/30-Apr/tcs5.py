# nums = [2, 7, 11, 15]
num = [3, 2, 4]
target = 6
dic = {}

for i in range(len(num)):
    if target - num[i] in dic:
        print([dic[target - num[i]], i])
    else:
        dic[num[i]] = i
        print(dic)

