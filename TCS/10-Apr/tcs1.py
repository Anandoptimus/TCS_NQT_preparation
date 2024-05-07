T = 3
N = 3
A = [1, 2, 3]
B = [3, 2, 1]
coins = 0

if T == 0:
    print('over')

while T > 0:
    max_val = max(B)
    max_ind = B.index(max_val)
    if T < A[max_ind]:
        coins += T * B[max_ind]
        print(coins)
        break

    coins += A[max_ind] * B[max_ind]
    T -= A[max_ind]
    A.pop(max_ind)
    B.pop(max_ind)
    if len(A) == 0:
        print('over')
        break
print(coins)