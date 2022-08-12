class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([x for x in nums if x > 0]))

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        cnt, delta = 0, 0
        for cur in nums:
            if cur > delta:
                cnt += 1
                delta = cur
        return cnt