class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        m = len(queries)
        idx = list(range(m))
        idx.sort(key = lambda j: queries[j])
        ans = [0]*m 
        cc = [0]*(n+1)
        logs.sort(key = lambda v: v[-1])
        left, right = 0, 0
        sz = len(logs)
        cur = 0
        for j in idx:
            t = queries[j]

            while right < sz and logs[right][-1] <= t:
                i = logs[right][0]
                if cc[i] == 0: cur += 1
                cc[i] += 1
                right += 1
            while left < sz and logs[left][-1] < t-x:
                i = logs[left][0]
                cc[i] -= 1
                if cc[i] == 0: cur -= 1
                left += 1
            ans[j] = n-cur
        return ans 
                
                
