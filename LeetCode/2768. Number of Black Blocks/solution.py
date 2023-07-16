class Solution:
    def countBlackBlocks(self, n: int, m: int, coordinates: List[List[int]]) -> List[int]:
        seen = set([(x,y) for x,y in coordinates])
        mp = [set() for _ in range(5)]
        tot = (n-1)*(m-1)
        for x, y in coordinates:
            for r in range(x-1,x+1):
                if 0 <= r < n-1:
                    for c in range(y-1,y+1):
                        if 0 <= c < m-1:
                            cnt = 0
                            for dr in [r,r+1]:
                                for dc in [c,c+1]:
                                    if (dr,dc) in seen:
                                        cnt += 1
                            mp[cnt].add((r,c))
        ans = [len(mp[i]) for i in range(5)]
        s = sum(ans)
        ans[0] = tot-s
        return ans 
