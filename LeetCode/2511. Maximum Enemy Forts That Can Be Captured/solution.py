class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans, cnt = 0, 0
        pre = -2
        for ch in forts:
            if ch == 0:
                cnt += 1
            else:
                if pre*ch == -1:
                    ans = max(ans, cnt)
                pre = ch 
                cnt = 0
        return ans 