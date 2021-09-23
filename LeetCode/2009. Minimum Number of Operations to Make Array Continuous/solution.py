class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums.sort()
        sz = len(nums)
        cnt = Counter()
        res = sz
        distinct = 0
        right = 0
        for left in range(sz):
            while right < sz and nums[right] < nums[left] + sz:
                if cnt[nums[right]] == 0:
                    distinct += 1
                cnt[nums[right]] += 1
                right += 1
            res = min(res, sz-distinct)
            cnt[nums[left]] -= 1
            if cnt[nums[left]] == 0:
                distinct -= 1
        return res