class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        @lru_cache(None)
        def dfs(i, j):
            if i < 0:
                return 0
            if j < 0:
                return float('inf')
            ans = dfs(i, j-1)
            cost = 0
            limit = factory[j][1]
            for k in range(limit):
                if i-k < 0:
                    break
                cost += abs(robot[i-k]-factory[j][0])
                ans = min(ans, cost+dfs(i-k-1,j-1))
            return ans 
        return dfs(n-1,m-1)