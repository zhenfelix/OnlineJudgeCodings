class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cc = Counter(nums)
        res = 0
        for i, s in enumerate(nums):
            n, m = len(s), len(target)
            cc[s] -= 1
            if target[-n:] == s:
                res += cc[target[:(m-n)]]
            cc[s] += 1
        return res