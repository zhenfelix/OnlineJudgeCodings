class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dp = defaultdict(int)
        dp[0], res, cur = 1, 0, 0
        for ch in word:
            bit = ord(ch)-ord('a')
            cur ^= (1<<bit)
            res += dp[cur]
            for i in range(10):
                res += dp[cur^(1<<i)]
            dp[cur] += 1
        return res