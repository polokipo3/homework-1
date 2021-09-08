def vr(N):
    d = N // (24 * 3600)
    h = (N - d * 24 * 3600) // 3600
    m = (N - d * 24 * 3600 - h * 3600) // 60
    s = N - d * 24 * 3600 - h * 3600 - m * 60
    if s > 0 and m == 0 and h == 0 and d == 0:
        return s, 'сек'
    elif s >= 0 and m > 0 and h == 0 and d == 0:
        return m, 'мин', s, 'сек'
    elif s >= 0 and m >= 0 and h > 0 and d == 0:
        return h, 'час', m, 'мин', s, 'сек'
    elif s >= 0 and m >= 0 and h >= 0 and d > 0:
        return d, 'дн', h, 'час', m, 'мин', s, 'сек'
A = list(map(int, input().split()))
for i in range(len(A)):
    print(vr(A[i]))
