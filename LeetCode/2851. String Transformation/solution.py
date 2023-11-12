MOD = 10**9+7

class KMP:
    def __init__(self, pattern):
        n = len(pattern)
        self.nxt = [-1]*(n)
        self.pattern = pattern
        for i in range(n-1):
            j = self.nxt[i]
            while pattern[i+1] != pattern[j+1] and j != -1:
                j = self.nxt[j]
            if pattern[j+1] == pattern[i+1]:
                j += 1
            self.nxt[i+1] = j
        # print(self.nxt)

    def find(self, s):
        n = len(s)
        m = len(self.pattern)
        ans = [0]*n 
        j = -1
        for i, ch in enumerate(s):
            while (j+1 == m or ch != self.pattern[j+1]) and j != -1:
                j = self.nxt[j]
            if ch == self.pattern[j+1]:
                j += 1
            if j+1 == m:
                ans[i] = 1 
        return ans 

def matmul(A,B):
    n, k = len(A), len(A[0])
    k, m = len(B), len(B[0])
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for p in range(k):
                C[i][j] += A[i][p]*B[p][j]
            C[i][j] %= MOD 
    return C 

def quickmul(A, q):
    ans = [[1,0],[0,1]]
    while q:
        if q&1:
            ans = matmul(ans,A)
        q >>= 1
        A = matmul(A,A)
    return ans 


class Solution:
    def numberOfWays(self, pattern: str, t: str, k: int) -> int:
        kmp = KMP(pattern)
        n = len(t)
        state = kmp.find(t+t)
        # print(state)
        cnt = sum(state[n:])
        flag = state[n-1]
        
        A = [[n-cnt-1,n-cnt],[cnt,cnt-1]]
        # print(A)
        A = quickmul(A,k)
        # print(A)
        return A[1][flag]