# cook your dish here
for i in range(int(input())):
    n = int(input())
    a= input()
    b=input()
    c=input()
    
    x = [0] * (n + 1)
    y = [0] * (n + 1)
    z = [0] * (n + 1)
    for i in range(n):
        if b[i]=='1' and c[i]=='0':d = 1
        elif b[i] == '0' and c[i] == '1':d = -1
        else:d = 0
            
            
        if a[i] == '0':
            x[i+1] = x[i] + d
            y[i+1] = y[i]
        else:
            x[i+1] = x[i]
            y[i+1] = y[i] + d
            
        z[i+1] = z[i] + d
        
    res = 0
    for p in [x, y, z]:
        p.sort()
        t = 0
        for i in range(n+1):
            res+= i*p[i]-t
            t += p[i]
    print(res//2)