# cook your dish here
for i in range(int(input())):
    x, y = map(int, input().split())
    print("Alice") if (x % 2 == 1) else print("Bob")