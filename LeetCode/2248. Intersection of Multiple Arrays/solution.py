class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans = set(nums[0])
        for cur in nums[1:]:
            ans &= set(cur)
        return sorted(list(ans))


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        cc = Counter(itertools.chain(*nums))
        n = len(nums)
        return sorted([k for k, v in cc.items() if v == n])