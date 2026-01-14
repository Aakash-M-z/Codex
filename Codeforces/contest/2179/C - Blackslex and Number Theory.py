for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    r = m
    u = 10**18
    for i in range(1, n):
        x = a[i]
        p = (x + 1) // 2
        q = x - m
        v = p if p > q else q
        if v < u:u = v
    c = u if u < a[1] else a[1]
    if c > r:
        r = c
    print(r)
    