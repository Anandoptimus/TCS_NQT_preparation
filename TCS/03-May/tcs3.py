import math

MAX = 2 **31 -1
MIN = -(2 ** 31)

x = 23454545488
res = 0
while x:
    digit = int(math.fmod(x, 10))
    x = int(x/ 10)
    if res >= MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
        print(0)
        break
    if res <= MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
        print(0)
        break
    res = res * 10 + digit

print(res)