class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dp = [0]*K
        dp[0] = 1
        cur, res = 0, 0
        for a in A:
            cur += a
            cur %= K
            res += dp[cur]
            dp[cur] += 1
        return res