DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 右下左上（顺时针）

class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        m, n = len(plate), len(plate[0])

        def check(x: int, y: int, d: int) -> bool:
            left = num
            while plate[x][y] != 'O':
                if left == 0: return False  # 无剩余步数
                if plate[x][y] == 'W':   d = (d + 3) % 4  # 逆时针
                elif plate[x][y] == 'E': d = (d + 1) % 4  # 顺时针
                x += DIRS[d][0]
                y += DIRS[d][1]
                if not (0 <= x < m and 0 <= y < n): return False  # 出界
                left -= 1
            return True

        ans = []
        for j in range(1, n - 1):
            if plate[0][j] == '.' and check(0, j, 1): ans.append([0, j])  # 上边
            if plate[-1][j] == '.' and check(m - 1, j, 3): ans.append([m - 1, j])  # 下边
        for i in range(1, m - 1):
            if plate[i][0] == '.' and check(i, 0, 0): ans.append([i, 0])  # 左边
            if plate[i][-1] == '.' and check(i, n - 1, 2): ans.append([i, n - 1])  # 右边
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/EXvqDp/solution/mei-ju-by-endlesscheng-5wzf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        n, m = len(plate), len(plate[0])
        visited = set()
        q = []
        dist = 0
        dij = [[-1,0],[0,1],[1,0],[0,-1]]
        ans = []
        for i in range(n):
            for j in range(m):
                if plate[i][j] == 'O':
                    for k in range(4):
                        q.append((i,j,k))
                        visited.add((i,j,k))
        while q:
            if dist > num:
                break
            nq = []
            for i, j, k in q:
                flag = False
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    if (i,j) not in [(0,0),(0,m-1),(n-1,0),(n-1,m-1)] and plate[i][j] == '.' and ((i == 0 and k == 0) or (i == n-1 and k == 2) or (j == 0 and k == 3) or (j == m-1 and k == 1)):
                        flag = True
                if flag:
                    ans.append([i,j])
                    continue
                di, dj = dij[k]
                di += i 
                dj += j 
                if di < 0 or di >= n or dj < 0 or dj >= m or plate[di][dj] == 'O':
                    continue
                if plate[di][dj] == 'W':
                    k = (k+1)%4
                elif plate[di][dj] == 'E':
                    k = (k-1)%4
                if (di,dj,k) in visited:
                    continue
                nq.append((di,dj,k))
                visited.add((di,dj,k))
            q = nq 
            dist += 1
        return ans