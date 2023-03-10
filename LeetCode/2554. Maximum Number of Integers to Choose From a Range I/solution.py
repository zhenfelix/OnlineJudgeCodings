class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        cnt, s = 0, 0
        for i in range(1,n+1):
            if i in banned: continue
            if s+i > maxSum: break
            s += i 
            cnt += 1
        return cnt
