a = 'ABCD'
c = ''
a = a.upper()
for i in a:
    car = ord(i) + 1
    c += chr(car)

print(c)