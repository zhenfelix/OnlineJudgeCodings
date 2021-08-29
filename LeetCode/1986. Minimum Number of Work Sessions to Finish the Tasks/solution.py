from functools import lru_cache
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()
        n = len(tasks)
        @lru_cache(None)
        def dfs(cur):
            if cur == 0:
                return 0
            delta = cur&(-cur)
            idx = 0
            while delta > (1<<idx):
                idx += 1
            sums = sessionTime-tasks[-idx-1]
            cur -= delta
            if sums == 0 or cur == 0:
                return 1+dfs(cur)
            s = cur
            res = float('inf')
            while True:
                i, t = 0, 0
                while (s>>i) > 0:
                    if (s>>i) & 1:
                        t += tasks[-i-1]
                    i += 1
                if t <= sums:
                    res = min(res, 1+dfs(cur-s))
                if s == 0:
                    break
                s = (s-1)&cur
            # print(cur,res,sums)
            return res
        return dfs((1<<n)-1)