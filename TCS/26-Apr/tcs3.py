# longest consective element
a = [0, 1, 6, -1]
n= 4
dic = {}
for i in a:
    dic[i] = False

longest = 0
for i in a:
    current = 1
    nextnum = i+1
    while (nextnum in dic) and not dic[nextnum]:
        current += 1
        dic[nextnum] = True
        nextnum += 1

    prevnum = i-1
    while (prevnum in dic) and not dic[prevnum] :
        current += 1
        dic[prevnum] = True
        prevnum -= 1

    longest = max(longest, current)



print(longest)


