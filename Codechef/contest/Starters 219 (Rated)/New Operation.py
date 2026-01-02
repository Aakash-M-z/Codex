# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    d = [[0]*n for _ in range(n)]
    for i in range(n): 
        d[i][i]=(a[i],a[i])

    for l in range(1,n):
        for i in range(n-l):
            j=i+l
            mn=float('inf')
            mx=-float('inf')
            for k in range(i,j):
                x = d[i][k][0]
                y = d[i][k][1]
                p = d[k+1][j][0]
                q = d[k+1][j][1]
                
                
                mn=min(mn,x+2*p,x+2*q,y+2*p,y+2*q)
                mx=max(mx,x+2*p,x+2*q,y+2*p,y+2*q)
            d[i][j]=(mn,mx)

    print(*d[0][n-1])