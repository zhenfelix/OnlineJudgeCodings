class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            idx, cc = 1<<i, 0
            for x in nums:
                if idx & x != 0:
                    cc += 1
            if cc%3 != 0:
                ans ^= idx
        if ans >= (1<<31):
            ans -= (1<<32)
        return ans
            