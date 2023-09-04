class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        @lru_cache(None)
        def dfs(i,j):
            if i == j:
                return True
            tot = sum(nums[i:j+1])
            s = 0
            for k in range(i,j):
                s += nums[k]
                if (s >= m or k == i) and dfs(i,k) and (tot-s >= m or k == j-1) and dfs(k+1,j):
                    return True
            return False
        return dfs(0,n-1)


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        for i in range(n-1):
            if nums[i]+nums[i+1] >= m:
                return True
        return False
