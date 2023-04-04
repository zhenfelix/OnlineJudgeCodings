class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        nums.sort()
        n = len(nums)
        s = [0]
        for a in nums:
            s.append(s[-1]+a)
        for q in queries:
            cnt = bisect_left(nums, q)
            ans.append(q*cnt-s[cnt]+s[-1]-s[cnt]-q*(n-cnt))
        return ans 