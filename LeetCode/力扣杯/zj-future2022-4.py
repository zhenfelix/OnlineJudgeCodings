class Solution:
    def minTransfers(self, distributions: List[List[int]]) -> int:
        cc = Counter()
        for a, b, v in distributions:
            cc[a] += v 
            cc[b] -= v
        arr = []
        for k, v in cc.items():
            if v != 0:
                arr.append(v)
        n = len(arr)
        balance = [0]*(1<<n)
        dp = [0]*(1<<n)
        tmp = dict()
        for i in range(n):
            tmp[1<<i] = arr[i]
        for s in range(1,1<<n):
            balance[s] = balance[s-(s&-s)] + tmp[s&-s]
            if balance[s] == 0:
                dp[s] = 1
        for s in range(1,1<<n):
            if balance[s] == 0:
                cur = mask = s  
                while True:
                    if balance[cur] == 0:
                        dp[s] = max(dp[s], dp[cur]+dp[mask^cur])
                    if cur == 0:
                        break
                    cur = (cur-1)&mask
        return n-dp[-1]

