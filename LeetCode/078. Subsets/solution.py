class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        q = deque([([],0)])
        while q:
            nq = []
            for tmp, idx in q:
                res.append(tmp.copy())
                for i in range(idx,n):
                    nq.append((tmp+[nums[i]],i+1))
            q = nq
        return res



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