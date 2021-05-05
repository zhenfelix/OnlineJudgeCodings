class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def func(x):
            if x > 0:
                return 1
            elif x == 0:
                return 0
            return -1
        cur = 1
        for x in nums:
            cur *= func(x)
        return cur 