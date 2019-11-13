class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        def dfs(n):
            if n in memo:
                return memo[n]
            if n == 1:
                memo[n] = 1
                return 1
            memo[n] = n
            for i in range(1,n-2):
                memo[n] = max(memo[n], dfs(i)*(n-i-1))
            return memo[n]

        memo = {}
        return dfs(N)