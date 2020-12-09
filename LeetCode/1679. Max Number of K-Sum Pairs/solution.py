class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cc = Counter()
        res = 0
        for x in nums:
            if cc[k-x] > 0:
                cc[k-x] -= 1
                res += 1
            else:
                cc[x] += 1
        return res 