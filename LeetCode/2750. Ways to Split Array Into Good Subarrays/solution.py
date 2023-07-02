class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10**9+7
        ans = 1
        cnt = 0
        flag = False
        for i, v in enumerate(nums):
            if v == 1:
                if flag:
                    ans *= (cnt+1)
                    ans %= MOD
                flag = True
                cnt = 0
            else:
                cnt += 1
        return ans if flag else 0