class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dfs(i):
            if i == n:
                return True
            if i == n-1:
                return False
            if nums[i] != nums[i+1]:
                if nums[i]+1 != nums[i+1]:
                    return False
                if i >= n-2 or nums[i+1]+1 != nums[i+2]:
                    return False
                return dfs(i+3)
            else:
                if dfs(i+2):
                    return True
                if i+2 < n and nums[i+1] == nums[i+2] and dfs(i+3):
                    return True
            return False
        return dfs(0)

