class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        cur = 0
        last = dict()
        for t in tasks:
            if t not in last:
                last[t] = cur
            else:
                cur = max(cur, last[t]+space+1)
                last[t] = cur
            cur += 1

        return cur 