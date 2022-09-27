from collections import *

def solve():
    n, k = list(map(int,input().split()))
    visidted = [False]*(n*2+1)
    visidted[n] = True 
    q = [n]
    cnt = 0
    ans = n-k
    while q:
        nq = []
        if ans == cnt:
            return ans 
        for cur in q:
            neib = [cur-1,cur+1]
            if cur%2 == 0:
                neib.append(cur//2)
            for nxt in neib:
                if 0 <= nxt <= n*2 and not visidted[nxt]:
                    visidted[nxt] = True 
                    if nxt == k:
                        return cnt+1
                    if nxt < k:
                        ans = min(ans, cnt+1+k-nxt)
                    else:
                        nq.append(nxt)
        q = nq 
        cnt += 1
    return -1


print(solve())