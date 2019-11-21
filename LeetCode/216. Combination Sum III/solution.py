class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(path, target):
            if len(path) == k:
                if target == 0:
                    res.append(path)
                return
            if target < 0:
                return
            start = 1
            if path:
                start = path[-1] + 1
            for i in range(start,10):
                dfs(path+[i], target-i)
            return

        res = []
        dfs([], n)
        return res


