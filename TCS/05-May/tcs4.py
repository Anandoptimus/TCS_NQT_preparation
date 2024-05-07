num = [23, 2, 4, 6, 70]
total = 0
remainder = {0: -1}
k = 6
for i, j in enumerate(num):
    total += j
    r = total % k
    if r not in remainder:
        remainder[r] = i
    elif i - remainder[r] > 1:
        # print(total)
        # print(remainder)
        print('True')
        break

