# cook your dish here
for i in range(int(input())):
    n,m = map(int,input().split())
    
    if n == 1:
        print((m+1) % 998244353)
        continue
    
    p = 1
    while p * 2 <= m:
        p *= 2

    x = 2*p -1
    ans = 2*m-x+1
    if ans < 0:
        ans = 0
    print(ans % 998244353)
        
    