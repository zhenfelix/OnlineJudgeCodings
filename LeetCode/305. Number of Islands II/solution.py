class Solution:
    def numIslands2(self, n: int, m: int, positions: List[List[int]]) -> List[int]:
        parent = dict()
        cnt = 0
        ans = []
        drc = [-1,0,1,0,-1]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def connect(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry 
            return True

        for r, c in positions:
            if (r,c) in parent:
                ans.append(cnt)
                continue
            parent[(r,c)] = (r,c)
            cnt += 1
            for dr, dc in zip(drc[1:],drc[:-1]):
                dr += r 
                dc += c 
                if dr < 0 or dr >= n or dc < 0 or dc >= m or (dr,dc) not in parent:
                    continue
                cnt -= connect((r,c),(dr,dc))
            ans.append(cnt)
        return ans 


