# maximum subarray
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

cursum = 0
maxsum = 0

for i in a:
    if cursum < 0:
        cursum = 0
    cursum += i
    maxsum = max(maxsum, cursum)

print(maxsum)