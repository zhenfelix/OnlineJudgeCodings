class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                isWater[i][j] -= 1
                if isWater[i][j] == 0:
                    q.append((i,j))
        while q:
            i, j = q.popleft()
            for di, dj in [[0,-1],[0,1],[-1,0],[1,0]]:
                di += i 
                dj += j
                if 0 <= di < n and 0 <= dj < m and isWater[di][dj] == -1:
                    isWater[di][dj] = isWater[i][j] + 1
                    q.append((di,dj))
        return isWater
