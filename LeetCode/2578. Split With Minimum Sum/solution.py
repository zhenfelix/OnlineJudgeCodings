class Solution:
    def splitNum(self, num: int) -> int:
        ans = 0
        base = 1
        s = sorted(str(num), reverse=True)
        n = len(s)
        for i in range(0,n,2):
            ans += (ord(s[i])-ord('0'))*base
            if i+1 < n:
                ans += (ord(s[i+1])-ord('0'))*base
            base *= 10  
        return ans 