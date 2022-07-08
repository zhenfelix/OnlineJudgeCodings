class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        j = 0
        ans = 0
        cur = 0
        for i in range(n):
            while j < n and tiles[j][-1]+1-tiles[i][0] <= carpetLen:
                cur += (tiles[j][-1]-tiles[j][0]+1)
                ans = max(ans, cur)
                j += 1
            if j < n and tiles[j][0]-tiles[i][0] <= carpetLen:
                ans = max(ans, cur+carpetLen-(tiles[j][0]-tiles[i][0]))
            cur -= (tiles[i][-1]-tiles[i][0]+1)
        return ans


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        ans = 0
        presums = [t[-1]-t[0]+1 for t in tiles]
        for i in range(1,n):
            presums[i] += presums[i-1]
        presums.append(0)

        for i in range(n):
            reach = tiles[i][0]+carpetLen-1
            j = bisect.bisect_right(tiles, [reach,float('inf')]) - 1
            ans = max(ans, presums[j]-presums[i-1]-max(0,tiles[j][-1]-reach))

        return ans