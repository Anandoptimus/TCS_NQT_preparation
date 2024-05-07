# letter combination of phone number

s = '11'
res = []
digitToString = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def backtrack(i, curstr):
    if len(curstr) == len(s):
        res.append(curstr)
        return

    for c in digitToString[s[i]]:
        backtrack(i+1, curstr+c)


if s:
    backtrack(0, "")
print(res)
