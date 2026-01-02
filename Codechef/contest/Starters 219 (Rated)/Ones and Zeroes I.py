# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    c,d = 0,0
    for i in s:
        if i == '1':c += 1
        else:c -= 1
        if c >= 0:
            d +=1

    print(d)