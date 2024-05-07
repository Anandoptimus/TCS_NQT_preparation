# Input: a[] = {1, 3, 4, 2, 6, 5, 8, 7}
# Output: Mean = 4.5, Median = 4.5

a = [1, 3, 4, 2, 6, 5, 8, 7]

# mean
mean = sum(a)/len(a)
print(mean)


a.sort()
n = len(a)
if n%2!= 0:
    z = float(a[n//2])
else:
    l = n//2
    # print(l)
    z = float((a[l-1] + a[l])/2.0)

print(z)