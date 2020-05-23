class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        original = image[sr][sc]
        if original == newColor: return image
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m or image[r][c] != original: return
            image[r][c] = newColor
            for dr, dc in [(0,-1),(0,1),(-1,0),(1,0)]:
                dfs(r+dr,c+dc)
            return
        dfs(sr,sc)
        return image