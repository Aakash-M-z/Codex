# cook your dish here
for i in range(int(input())):
    n = int(input())
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))

    c = 1
    mx = float('-inf')

    for i in range(n):
        if b[i] < a[i]:
            c = 0
            break
        if b[i] > a[i] and a[i]<=mx:
            c = 0
            break
        mx = max(mx,a[i])

    print("Yes") if  c else print("No")