a = '3[a3[b]1[ab]]'
s = []
cur_str = ''
cur_num = 0

for c in a:
    if c.isdigit():
        cur_num = cur_num * 10 + int(c)

    elif c == '[':
        s.append(cur_num)
        s.append(cur_str)
        cur_num = 0
        cur_str = ''

    elif c == ']':
        pre_str = s.pop()
        pre_num = s.pop()
        cur_str = pre_str + cur_str * pre_num

    else:
        cur_str += c


while s:
    cur_str = s.pop() + cur_str

print(cur_str)