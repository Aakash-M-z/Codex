for _ in range(int(input())):
    n = int(input())
    a = input()
    b= input()
    c=input()
    d0,d1= 0,0
    
    
    for i in range(n):
        v = (b[i]=='1') - (c[i]=='1')
        if a[i] == '0': d0 += v
        else: d1+= v
    print(max(abs(d0),abs(d1))) if d0 * d1 < 0 else print(abs(d0) + abs(d1))