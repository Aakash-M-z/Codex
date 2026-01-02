# cook your dish here
for i in range(int(input())):
    n = int(input())
    if n == 2:
        print(-1)
        continue
    a = [[0]*n for _ in range(n)]
    a[0][0] = 1
    a[0][1] = 1
    a[0][2] = 1
    a[1][1] = 1
    a[1][2] = 1
    a[2][1] = 1
    a[2][2] = 1
    for i in range(2, n):
        a[i][2] = 1
    for j in range(2, n):
        a[n-1][j] = 1
    for i in a:
        print(*i)