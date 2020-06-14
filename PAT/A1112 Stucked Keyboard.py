import sys, heapq
from collections import *
from functools import cmp_to_key



# sys.stdin = open('input.txt', 'r')
k = int(input())
s = input()
n = len(s)
candidates = set(s)
res = ''
keys = ''
i = 0
while i < n:
    if s[i] in candidates:
        if s[i:i+k] != s[i]*k:
            candidates.remove(s[i])
            i += 1
        else:
            i += k
    else:
        i += 1
i = 0
while i < n:
    res += s[i]
    if s[i] in candidates:
        i += k
    else:
        i += 1
for ch in s:
    if ch in candidates:
        keys += ch
        candidates.remove(ch)
print(keys)
print(res)