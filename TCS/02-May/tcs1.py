s = '2[a2[b]]'
cs = ''
cn = 0
cl = []

for c in s:
    if c.isdigit():
        # print(int(c))///
        cn = cn * 10 + int(c)
        # print(cn)////

    elif c == '[':
        cl.append(cn)
        cl.append(cs)
        cs = ''
        cn = 0

    elif c == ']':
        print(cl)
        ps = cl.pop()
        pn = cl.pop()
        cs = ps + cs * pn


    else:
        cs += c

while cl:
    print(cl)
    cs = cl.pop() + cs

print(cs)
