class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n)[::-1]:
            p, b = questions[i]
            dp[i] = max(dp[i+1], p+dp[i+b+1] if i+b+1 <= n else p)
        # print(dp)
        return dp[0]