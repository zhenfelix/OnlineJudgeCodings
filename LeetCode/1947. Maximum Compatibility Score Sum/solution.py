from functools import lru_cache
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])
        @lru_cache(None)
        def dfs(state, idx):
            if state == 0:
                return 0
            return max(sum(students[idx][j]==mentors[i][j] for j in range(n))+dfs(state-(1<<i),idx+1) for i in range(m) if (state>>i)&1)

        return dfs((1<<m)-1, 0)