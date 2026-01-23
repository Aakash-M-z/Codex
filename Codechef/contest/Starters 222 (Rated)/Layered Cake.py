t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    count = 0
    for a in A:
        for b in B:
            if b < a:
                count += 1
    
    print(count) 