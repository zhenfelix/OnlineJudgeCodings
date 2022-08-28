# https://leetcode.cn/contest/ubiquant2022/ranking/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> int:
        cc = Counter()
        for x in nums:
            y = int(str(x)[::-1])
            cc[x-y] += 1
        ans = 0
        MOD = 10**9+7
        for k, v in cc.items():
            ans += v*(v-1)//2
            ans %= MOD
        return ans