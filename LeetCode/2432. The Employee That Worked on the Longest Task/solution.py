class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        idx, ans = n, -1
        cur = 0
        for i, t in logs:
            delta = t-cur
            if delta > ans or (delta == ans and i < idx):
                ans = delta
                idx = i 
            cur = t 
        return idx