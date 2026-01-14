# cook your dish here
# cook your dish here
for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = float('inf')
    for i in range(n):
        c = min(c, max(l[i],l[i+1]))
    
    print(c)