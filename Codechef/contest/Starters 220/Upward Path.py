# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    x1,x2 = 1,1
    if a[0] <= b[0]:y1 = 1
    else:y1 = 0
    if b[0] <= a[0]:y2 = 1
    else:y2 = 0
    
    for i in range(1, n):
        t1 = (x1 and a[i-1] <= a[i]) or (x2 and b[i-1] <= a[i])
        t2 = (x1 and a[i-1] <= b[i]) or (x2 and b[i-1] <= b[i])
        
        u1 = (y1 and b[i-1] <= b[i]) or (y2 and a[i-1] <= b[i]) or (t1 and a[i] <= b[i])
        u2 = (y1 and b[i-1] <= a[i]) or (y2 and a[i-1] <= a[i]) or (t2 and b[i] <= a[i])
        
        if t1:x1 = 1
        else:x1 = 0

        if t2:x2 = 1
        else:x2 = 0

        if u1:y1 = 1
        else:y1 = 0

        if u2:y2 = 1
        else:y2 = 0
    print("yes" if y1 or y2 else "no")


