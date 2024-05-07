# Input: arr[] = {{11, 20}, {30, 40}, {5, 10}, {40, 30}, {10, 5}}
# Output: Following pairs have symmetric pairs
#         (30, 40)
#         (5, 10)

arr = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]

# print(len(arr))
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i][0] == arr[j][1] and arr[i][1] == arr[j][0]):
            print(f"{arr[i][0] , arr[i][1]}")
