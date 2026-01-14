# cook your dish here
for i in range(int(input())):
    n = int(input())
    
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))


    m = float('inf')
    s = 0
    for i in range(n):
        m = min(m, c[i])
        s += a[i] * m

    print(s)
