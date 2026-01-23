# cook your dish here
import math

n,k = map(int,input().split())

s = int(math.sqrt(n))
a = []
for i in range(s):
    a.append([])


for i in range(1,n+1):
    a[(i-1)%s].append(i)

for x in reversed(a):
    print(*x, end=" ")
print()


