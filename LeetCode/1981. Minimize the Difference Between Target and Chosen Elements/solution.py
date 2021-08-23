class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        dp = [0]
        mx = float('inf')
        n, m = len(mat), len(mat[0])
        for i in range(n):
            visited = set()
            mx += min(mat[i][j] for j in range(m))
            for j in range(m):
                for x in dp:
                    if x+mat[i][j] > target:
                        mx = min(mx, x+mat[i][j])
                    else:
                        visited.add(x+mat[i][j])
            dp = list(visited)
            # print(sorted(dp))
        return min(target-max(dp, default=-float('inf')),mx-target)


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        dp = {0}
        mx = float('inf')
        for row in mat:
            ndp = set()
            mx += min(x for x in row)
            for x in row:
                for y in dp:
                    if x+y > target:
                        mx = min(mx, x+y)
                    else:
                        ndp.add(x+y)
            dp = ndp
            # print(sorted(dp))
        return min(target-max(dp, default=-float('inf')),mx-target)


class Solution:
    def minimizeTheDifference(self, mat, target):
        possible_min = sum(min(row) for row in mat)
        if possible_min > target: return possible_min - target
        
        nums = {0}
        for row in mat:
            nums = {x + i for x in row for i in nums if x + i <= 2*target - possible_min}
        
        return min(abs(target - x) for x in nums)