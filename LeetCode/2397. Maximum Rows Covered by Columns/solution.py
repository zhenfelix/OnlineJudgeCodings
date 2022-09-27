class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        n, m = len(mat), len(mat[0])
        def check(i, s):
            for j in range(m):
                if mat[i][j] == 1 and (((s>>j)&1) == 0):
                    return False
            return True

        ans = 0
        for ss in range(1<<m):
            if bin(ss)[2:].count('1') == cols:
                tmp = sum(check(i,ss) for i in range(n))
                ans = max(ans,tmp)
        return ans