# cook your dish here
for i in range(int(input())):
    n,x,k = map(int,input().split())
    
    c = x 
    for i in range(0,n+1,k):
        c = min(c,abs(x-i))
        
    print(c)