class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        arr = []
        for i in range(3):
            for j in range(3):
                for _ in range(grid[i][j]):
                    arr.append((i,j))
        @lru_cache(None)
        def dfs(i,s):
            if i == 9: return 0
            ans = inf 
            cr, cc = arr[i]
            for j in range(9):
                if (s>>j)&1 == 0:
                    r, c = j%3, j//3
                    ans = min(ans,abs(r-cr)+abs(c-cc)+dfs(i+1,s|(1<<j)))
            return ans 

        return dfs(0,0) 



start = tuple([1] * 9)
saved = {start: 0}
dq = deque([start])
while dq:
    u = dq.popleft()
    lst_u = list(u)
    for i in range(9):
        if lst_u[i] >= 1:
            x, y = divmod(i, 3)
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < 3 and 0 <= new_y < 3:
                    new_i = new_x * 3 + new_y
                    lst_u[i] -= 1
                    lst_u[new_i] += 1
                    tp = tuple(lst_u)
                    if tp not in saved:
                        saved[tp] = saved[u] + 1
                        dq.append(tp)
                    lst_u[i] += 1
                    lst_u[new_i] -= 1

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        vals = []
        for x in grid: vals.extend(x)
        return saved[tuple(vals)]


# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/DihZU2/view/CBMWts/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。