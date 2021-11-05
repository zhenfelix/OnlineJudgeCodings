class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diff = [0]*n 
        tot = sum(nums)
        pre = nums[0]
        for i in range(1,n):
            diff[i] = pre-(tot-pre)
            pre += nums[i]
        left, right = Counter(), Counter(diff[1:])
        res = right[0]
        for i in range(n):
            if i:
                left[diff[i]] += 1
                right[diff[i]] -= 1
            delta = k-nums[i]
            res = max(res, left[delta]+right[-delta])
        return res

