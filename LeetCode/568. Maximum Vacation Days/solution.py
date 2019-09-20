class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        n = len(flights)
        for i in range(n):
            flights[i][i] = 1
        
        k = len(days[0])
        dp = [-float('inf')]*n
        dp[0] = 0
        for day in range(k):
            tmp = dp.copy()
            for end in range(n):
                for start in range(n):
                    if flights[start][end] == 1:
                        tmp[end] = max(tmp[end], dp[start]+days[end][day])
            dp = tmp
        return max(dp)