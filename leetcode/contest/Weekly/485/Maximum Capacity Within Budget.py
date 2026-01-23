class Solution:
    def maxCapacity(self, c, a, b):
        n = len(c)
        p = sorted(range(n), key=lambda i: c[i])

        r,x = 0,0
        y = [0] * n

        for i in range(n):
            u = p[i]
            if c[u] < b:
                r = max(r, a[u])
            x = max(x, a[u])
            y[i] = x

        t = n - 1
        for i in range(n):
            u = p[i]
            while t >= 0 and c[u] + c[p[t]] >= b:
                t -= 1
            
            v = min(t,i - 1)
            if v >= 0:
                r = max(r, a[u] + y[v])

        return r