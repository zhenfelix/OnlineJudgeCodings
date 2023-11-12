import sys
import random
from heapq import heappop, heappush
from types import GeneratorType
from math import sqrt, gcd, inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())



class PrimeTable:
    def __init__(self, n: int) -> None:
        self.n = n
        self.primes = primes = []
        self.min_div = min_div = [0] * (n + 1)
        min_div[1] = 1

        for i in range(2, n + 1):
            if not min_div[i]:
                primes.append(i)
                min_div[i] = i
            for p in primes:
                if i * p > n: break
                min_div[i * p] = p
                if i % p == 0:
                    break

    def prime_factorization(self, x: int):
        n, min_div = self.n, self.min_div
        for p in range(2, int(x ** 0.5) + 1):
            if x <= n: break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        while 1 < x <= n:
            p, cnt = min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= n and x > 1:
            yield x, 1


pt = PrimeTable(10 ** 6)


def solve():
    n, a, b = RI()
    arr = RILST()
    gra = [[] for _ in range(10 ** 6)]
    for i, y in enumerate(arr, start=1):
        s = 0
        for x, y in pt.prime_factorization(y):
            s += x * y
        s = s % n + 1
        p = s + n + 1
        gra[i].append((p, 1))
        gra[p].append((i, 1))
        if s <= n:
            gra[s].append((i, 2))
            gra[i].append((s, 2))

    h = [(0, a)]
    dist = [inf] * (10 ** 6)
    dist[a] = 0
    while h:
        c, x = heappop(h)
        if c > dist[x]:
            continue
        if x == b:
            print(c >> 1)
            return
        for y, w in gra[x]:
            d = c + w
            if d < dist[y]:
                dist[y] = d
                heappush(h, (d, y))

    print(-1)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()