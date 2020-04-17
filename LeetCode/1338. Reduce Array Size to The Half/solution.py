from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        cc = Counter(arr)
        nums = sorted(cc.values(), key=lambda x:-x)
        res, cnt = 0, 0
        while cnt*2 < n:
            cnt += nums[res]
            res += 1
        return res