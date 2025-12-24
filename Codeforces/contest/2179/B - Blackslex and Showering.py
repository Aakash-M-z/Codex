for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dif = 0
    for i in range(n - 1):
        dif += abs(a[i] - a[i + 1])
    ans = dif
    t = dif - abs(a[0] - a[1])
    if t < ans:
        ans = t
    t = dif - abs(a[n - 2] - a[n - 1])
    if t < ans:
        ans = t
    for i in range(1, n - 1):
        t = dif
        t -= abs(a[i] - a[i - 1])
        t -= abs(a[i] - a[i + 1])
        t += abs(a[i - 1] - a[i + 1])
        if t < ans:
            ans = t
    print(ans)