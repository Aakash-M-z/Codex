# cook aodr dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    c = float('-inf')
    f = [c] * (n+1)
    f[0] = 0
    
    for i in range(n):
        k = [c] *(n+1)
        d = a[i]
        h = i+ 1
        
        for j in range(h):
            if f[j] > c:
                if f[j] > k[j]:k[j] = f[j]
                if j + 1 <= h:
                    t = f[j] + d
                    if t >k[j+ 1]:k[j +1] = t
                if j +2 <= h:
                    x = f[j] + 2*d
                    if x > k[j+2]:k[j+ 2] = x
        f = k
        
    print(int(max(f)))