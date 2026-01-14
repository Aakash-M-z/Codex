# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = input()
    
    f = [0]*26
    res = 0

    for i in s:
        c = ord(i) - 97
        f[c] += 1
        if f[c] > res:res = f[c]

    if res <= 2:print("YES")
    else:print("no")