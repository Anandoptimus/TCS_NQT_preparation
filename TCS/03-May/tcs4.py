# mininum number of bracket reversals needed to make an expression
s = '][[]'
close, maxclose = 0, 0

for c in s:
    if c == '[':
        close += 1
    else:
        close -= 1

    maxclose = max(close, maxclose)

print((maxclose + 1) // 2)
