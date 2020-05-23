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
n, k = map(int, input().split(' '))
windows = [str2clock("08:00:00")] * k
people = []
for i in range(n):
    enter, duration = input().split(' ')
    people.append((str2clock(enter), int(duration) * 60))
people = deque(sorted(people))
waiting = []


# for enter, duration in people:
#     if enter > str2clock("17:00:00"):
#         break
#     if windows[0] <= enter:
#         waiting.append(0)
#         heapq.heappush(windows,enter+min(duration,3600))
#         heapq.heappop(windows)
#     else:
#         waiting.append(windows[0]-enter)
#         heapq.heappush(windows,windows[0]+min(duration,3600))
#         heapq.heappop(windows)

# for t in range(str2clock("08:00:00"), str2clock("17:00:01")):
#     while people and people[0][0] <= t and windows[0] <= t:
#         enter, duration = people.popleft()
#         heapq.heappop(windows)
#         heapq.heappush(windows, t + min(duration, 3600))
#         waiting.append(t - enter)

# for enter, duration in people:
#     if enter > str2clock("17:00:00"):
#         continue
#     t = max(enter,windows[0])
#     heapq.heappop(windows)
#     heapq.heappush(windows,t+min(duration,3600))
#     waiting.append(t - enter)

start, end = str2clock("08:00:00"), str2clock("17:00:00")
people = deque([p for p in people if p[0] <= end])
t = start
while people:
    while people and people[0][0] <= t and windows[0] <= t:
        enter, duration = people.popleft()
        heapq.heappop(windows)
        heapq.heappush(windows, t + min(duration, 3600))
        waiting.append(t - enter)
    t += 1


print(str(round(sum(waiting) / (60 * len(waiting)), 1)) if waiting else "0.0")








