class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = 0
        color = [0]*n 
        res = []
        for i, c in queries:
            oc = color[i]
            if i:
                if color[i-1] == oc:
                    ans -= (oc > 0)
                if color[i-1] == c:
                    ans += (c > 0)
            if i+1 < n:
                if color[i+1] == oc:
                    ans -= (oc > 0)
                if color[i+1] == c:
                    ans += (c > 0)
            color[i] = c 
            res.append(ans)
        return res 