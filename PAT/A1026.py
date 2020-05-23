import sys, heapq
from collections import *

def clock2str(t):
    s = t%60
    t //= 60
    m = t%60
    t //= 60
    h = t
    return  str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)

def str2clock(hms):
    h, m, s = map(int,hms.split(':'))
    return h*3600+m*60+s

def convert(delta):
    return delta//60 + (delta%60 >= 30)

# sys.stdin = open('input.txt', 'r')
n = int(input())
people = []
for i in range(n):
    enter, duration, flag = input().split(' ')
    people.append((str2clock(enter),int(duration)*60,int(flag)))
people = deque(sorted(people))
k, m = map(int, input().split(' '))
viptables = list(map(int, input().split(' ')))
isviptable = set(viptables)
tables = [i+1 for i in range(k) if i+1 not in isviptable]
heapq.heapify(viptables)
heapq.heapify(tables)
q, vipq = deque(), deque()
occupy = []
cnt = [0]*(k+1)
waiting = []
for t in range(str2clock("08:00:00"),str2clock("21:00:00")):
    while occupy and occupy[0][0] <= t:
        _, tab = heapq.heappop(occupy)
        if tab in isviptable:
            heapq.heappush(viptables,tab)
        else:
            heapq.heappush(tables,tab)
    if people and people[0][0] <= t:
        enter, duration, flag = people.popleft()
        if flag == 1:
            vipq.append((enter,duration))
        else:
            q.append((enter,duration))
    if viptables and vipq:
        tab = heapq.heappop(viptables)
        enter, duration = vipq.popleft()
        cnt[tab] += 1
        waiting.append((clock2str(enter),clock2str(t),str(convert(t-enter))))
        heapq.heappush(occupy, (t+min(duration,120*60),tab))
    while (tables or viptables) and (q or vipq):
        if tables and viptables:
            if tables[0] < viptables[0]:
                tab = heapq.heappop(tables)
            else:
                tab = heapq.heappop(viptables)
        elif tables:
            tab = heapq.heappop(tables)
        else:
            tab = heapq.heappop(viptables)
        if q and vipq:
            if q[0][0] < vipq[0][0]:
                enter, duration = q.popleft()
            else:
                enter, duration = vipq.popleft()
        elif q:
            enter, duration = q.popleft()
        else:
            enter, duration = vipq.popleft()
        cnt[tab] += 1
        waiting.append((clock2str(enter), clock2str(t), str(convert(t - enter))))
        heapq.heappush(occupy, (t + min(duration, 120*60), tab))
waiting.sort(key=lambda x: x[1])
for w in waiting:
    print(' '.join(w))
print(' '.join([str(x) for x in cnt[1:]]))








