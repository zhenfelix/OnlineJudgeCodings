class Solution:
    def numberOfUniqueGoodSubsequences(self, s: str) -> int:
        MOD = 10**9+7
        n = len(s)
        dp = [0]*2
        cnt = 1
        flag = 0
        for i in range(n)[::-1]:
            cur = int(s[i])
            if cur == 0:
                flag = 1
            dp[cur] = (dp[cur]+dp[1-cur]+1)%MOD
        # print(dp)
            
        return (dp[1]+flag)%MOD

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        MOD = 10**9+7
        leaf, half, full = 1, [0,0], 0
        for ch in binary[::-1]:
            idx = ord(ch)-ord('0')
            leaf, half[idx], half[1-idx], full = leaf+half[1-idx], half[idx]+leaf, 0, full+half[1-idx]
            leaf %= MOD
            half[idx] %= MOD
            full %= MOD
            # print(leaf, half, full)
        return (full+half[1]+('0' in binary))%MOD