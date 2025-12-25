# cook your dish here
for i in range(int(input())):
    n = int(input())
    res = (n% 4 == 0) or (n < 7 and n!= 5)
    print("Yes" if res else "No")