import sys, heapq
from collections import *
from functools import cmp_to_key



# sys.stdin = open('input.txt', 'r')
n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()
print(n%2,sum(arr[n//2:])-sum(arr[:n//2]))
