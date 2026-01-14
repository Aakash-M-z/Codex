# cook your dish here
for i in range(int(input())):
    s = input()
    l = int(s[-1])
    if l % 2:
        print(0)
        continue
    f = 0
    for c in s:
        if int(c) % 2:
            f = 1
            break
    if f or f!=0:
        print(1)
        continue
    if len(s) == 1:
        print(-1)
        continue
    f = 0
    for c in s:
        if int(c) > l:
            f = 1
            break
    print(2) if f!=0 else print(3)
