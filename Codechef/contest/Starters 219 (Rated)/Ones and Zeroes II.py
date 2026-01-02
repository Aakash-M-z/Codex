# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(input().strip())

    c = a.count('1')
    m = c + min(c, n - c)
    b,s,k = 0,0,0

    for i in range(n):
        if a[i] == '1':
            b += 1
        else:
            b -= 1

        if b < 0:
            if k < i:
                k = k
            if k < i + 1:
                k = i + 1
            while k < n and (a[k] == '0' or k < i):
                if a[k] == '0':
                    k += 1
                else:
                    k += 0
            if k >= n:
                break
            if k - i >= 0:
                s += k - i
            else:
                s += 0
            if b <= -1:
                b += 2
            a[k] = '0'

    print(m, s)
