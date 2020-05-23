import sys, heapq
from collections import *


def clock2str(t):
    s = t % 60
    t //= 60
    m = t % 60
    t //= 60
    h = t
    return str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2)


def str2clock(hms):
    h, m, s = map(int, hms.split(':'))
    return h * 3600 + m * 60 + s


# sys.stdin = open('input.txt', 'r')
N, M, K, Q = map(int, input().split(' '))
people = map(int, input().split(' '))
people = deque([(i+1, p*60) for i, p in enumerate(people)])
res = {}
qs = defaultdict(deque)

for _ in range(M-1):
    for n in range(N):
        if people:
            qs[n].append(people.popleft())

cur = str2clock('08:00:00')
pq = [(cur,n,-1) for n in range(N)]

while pq:
    # print(qs,pq)
    cur, n, _ = heapq.heappop(pq)
    if cur >= str2clock('17:00:00'):
        break
    if qs[n]:
        i, p = qs[n].popleft()
        cur += p
        heapq.heappush(pq,(cur,n,i))
        res[i] = clock2str(cur)
    if people:
        qs[n].append(people.popleft())

queries = map(int, input().split(' '))
for query in queries:
    if query not in res:
        print('Sorry')
    else:
        print(res[query][:-3])









