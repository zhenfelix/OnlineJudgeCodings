class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        @lru_cache(None)
        def dfs(i, j, cnt):
            if i == 0 and j == 0 and cnt == 1 and grid[i][j] == '(':
                return True
            if i < 0 or j < 0 or cnt < 0:
                return False
            if grid[i][j] == '(':
                delta = 1
            else:
                delta = -1
            return dfs(i-1,j,cnt-delta) or dfs(i,j-1,cnt-delta)
        return dfs(n-1,m-1,0)


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        if (n+m)%2 == 0 or grid[0][0] == ')' or grid[-1][-1] == '(':
            return False
        @lru_cache(None)
        def dfs(i, j, cnt):
            if cnt > i+j+1:
                return False
            if i == 0 and j == 0:
                return cnt == 1
            if i < 0 or j < 0 or cnt < 0:
                return False
            if grid[i][j] == '(':
                delta = 1
            else:
                delta = -1
            return dfs(i-1,j,cnt-delta) or dfs(i,j-1,cnt-delta)
        return dfs(n-1,m-1,0)


class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(': return False  # 剪枝

        @cache  # 效果类似 vis 数组
        def dfs(x: int, y: int, c: int) -> bool:
            if c > m - x + n - y - 1: return False  # 剪枝：即使后面都是 ')' 也不能将 c 减为 0
            if x == m - 1 and y == n - 1: return c == 1  # 终点一定是 ')'
            c += 1 if grid[x][y] == '(' else -1
            return c >= 0 and (x < m - 1 and dfs(x + 1, y, c) or y < n - 1 and dfs(x, y + 1, c))  # 往下或者往右
        return dfs(0, 0, 0)  # 起点


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/check-if-there-is-a-valid-parentheses-string-path/solution/tian-jia-zhuang-tai-hou-dfscpythonjavago-f287/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。