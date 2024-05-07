import timeit


# Define your code snippet
code_snippet = """
from collections import OrderedDict
n = int(input())
a = list(map(int, input().split()))
k = int(input())
dic = OrderedDict()
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

c = 0
for i in dic:
    if dic[i] == k:
        print(i)
        c = 1
        break
if c == 0 :
    print(-1)
"""

# Run the code snippet and measure execution time
execution_time = timeit.timeit(stmt=code_snippet, number=1)

# Print the execution time
print("Execution time:", execution_time)
