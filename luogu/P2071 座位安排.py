import sys, collections

sys.stdin = open('input.txt', 'r')
graph = collections.defaultdict(list)
n = int(input())
for i in range(n*2):
    a, b = map(int, input().split(' '))
    graph[n*2+i] += [a*2-2,a*2-1,b*2-2,b*2-1]


def hungarian():
    res = 0
    match = [-1]*(4*n)
    for i in range(n*2,n*4):
        if match[i] == -1:
            visited = set()
            if dfs(i,visited,match):
                res += 1
    return res

def dfs(cur, visited_, match_):
    for nxt in graph[cur]:
        if nxt not in visited_:
            visited_.add(nxt)
            if match_[nxt] == -1 or dfs(match_[nxt], visited_, match_):
                match_[cur] = nxt
                match_[nxt] = cur
                return True
    return False

print(hungarian())