# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l = set()
    c = 0

    
    for i in a:
        if i == 1 or (i-1) in l:
            l.add(i)
            c += 1
            
    print(c)