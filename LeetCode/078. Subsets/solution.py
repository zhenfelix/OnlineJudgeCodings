class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i,path):
            if i == n:
                res.append(path.copy())
                return
            dfs(i+1,path)
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            return
        dfs(0,[])
        return res