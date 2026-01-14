# cook your dish here
for i in range(int((input()))):
    n = int(input())
    s = input()
    c,a = 0,0
    
    for i in range(n+1):
        if i > 0 and s[i-1] == '1': c+=1 
        if 2*c > i:a+=1 
    print(a)