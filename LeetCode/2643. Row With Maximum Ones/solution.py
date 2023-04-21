class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [-1,-1]
        for i, row in enumerate(mat):
            cnt = row.count(1)
            if cnt > ans[-1]:
                ans[0] = i 
                ans[1] = cnt
        return ans 