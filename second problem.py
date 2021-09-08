def st(n):
    k = 0
    while 10 ** k < n:
        k += 1
    return k
def su(n):
    k = st(n)
    s = 0
    while k != - 1:
        s += ((n - ((n // (10 ** (k + 1))) * (10 ** (k + 1)))) // (10 ** k))
        k -= 1
    return s
A = []
A = [x for x in range(1, 1001, 2)]
A = [x ** 3 for x in A if su(x ** 3) % 7 == 0]
sum1 = 0
for i in range(len(A)):
    sum1 += A[i]
print(sum1)
A = [x ** 3 for x in range(1, 1001, 2)]
A = [x + 17 for x in A if su(x + 17) % 7 == 0]
sum2 = 0
for i in range(len(A)):
    sum2 += A[i]
print(sum2)