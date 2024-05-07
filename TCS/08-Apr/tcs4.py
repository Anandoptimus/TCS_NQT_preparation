# def firstNonRepeating(arr, n):
#     # Complete the function
#     dic = {}
#     for i in range(n):
#         if arr[i] in dic:
#             dic[arr[i]] += 1
#         else:
#             dic[arr[i]] = 1
#     print(dic)
#     for i in dic:
#         print(i)
#     for i, j in dic.items():
#         if j == 1:
#             return i
#     return 0
#
# arr = [4, -8, 1, -4, -3, -8, -3, -10, 3, -3, 10]
# n = 11
# print(firstNonRepeating(arr, n))

arr = [1, 2, 3, 2, 1, 2, 2]

a = set()
aa = []
b = set()

for i in range(len(arr)):
    if arr[i] not in a:
        a.add(arr[i])
        aa.append(arr[i])
    else:
        b.add(arr[i])
print(a, aa, b)

for i in range(len(a)):
    if aa[i] not in b:
        print(aa[i])

n = 1
print(-n)
