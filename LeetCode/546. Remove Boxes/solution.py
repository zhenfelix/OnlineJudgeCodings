from functools import lru_cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dfs(i,j,cnt):
            if i > j:
                return 0
            if i == j:
                return cnt*cnt
            k = i
            while k+1 <= j and boxes[i] == boxes[k+1]:#important to speed up
                k += 1
            i, cnt = k, cnt+k-i
            res = cnt*cnt + dfs(i+1,j,1)
            for k in range(i+1,j+1):
                if boxes[i] == boxes[k]:
                    res = max(res,dfs(i+1,k-1,1)+dfs(k,j,cnt+1))
            return res
        return dfs(0,len(boxes)-1,1)