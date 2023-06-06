class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                g[x].append((i, j))  # 相同元素放在同一组，统计位置

        ans = 0
        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in sorted(g.items(), key=lambda p: p[0]):
            # 先把最大值算出来，再更新 row_max 和 col_max
            mx = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            ans = max(ans, max(mx))
            for (i, j), f in zip(pos, mx):
                row_max[i] = max(row_max[i], f)  # 更新第 i 行的最大 f 值
                col_max[j] = max(col_max[j], f)  # 更新第 j 列的最大 f 值
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/maximum-strictly-increasing-cells-in-a-matrix/solution/dong-tai-gui-hua-you-hua-pythonjavacgo-b-axv0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rv = [[0]*2 for _ in range(n)]
        cv = [[0]*2 for _ in range(m)]
        rmx = [-inf]*n 
        cmx = [-inf]*m 
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append((mat[i][j],i,j))
        arr.sort()
        ans = 0
        for v, i, j in arr:
            cur = 0
            if v > rmx[i]:
                cur = max(cur, rv[i][-1]+1)
            else:
                cur = max(cur, rv[i][0]+1)
            if v > cmx[j]:
                cur = max(cur, cv[j][-1]+1)
            else:
                cur = max(cur, cv[j][0]+1)
            ans = max(ans,cur)
            if v > rmx[i]:
                rmx[i] = v 
                rv[i][0] = max(rv[i][0],rv[i][-1])
            rv[i][-1] = max(rv[i][-1],cur)
            if v > cmx[j]:
                cmx[j] = v 
                cv[j][0] = max(cv[j][0],cv[j][-1])
            cv[j][-1] = max(cv[j][-1],cur)
        return ans 
