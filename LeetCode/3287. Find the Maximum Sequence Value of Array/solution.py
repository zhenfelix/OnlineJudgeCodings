class Solution:
    def maxValue(self, nums: List[int], K: int) -> int:
        n = len(nums)
        limit = (1<<7)

        def calc(arr):
            dp = [[[0]*limit for _ in range(n+1)] for _ in range(K+1)]
            dp[0][0][0] = 1
            for i in range(n):
                y = arr[i]
                for j in range(K+1):
                    for x in range(limit):
                        if dp[j][i][x]:
                            dp[j][i+1][x] = 1
                            if j+1 <= K:
                                dp[j+1][i+1][x|y] = 1
            return dp[K]
        left, right = calc(nums), calc(nums[::-1])
        ans = 0
        for i in range(K,n-K+1):
            for x in range(limit):
                if left[i][x]:
                    for y in range(limit):
                        if right[n-i][y]:
                            ans = max(ans,x^y)
        return ans 

