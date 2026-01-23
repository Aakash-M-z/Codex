# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    res = 0
    for i in range(n,0,-1):
        if a[i-1]!=i:
            res = a[i-1]
            break
            
    print(res)