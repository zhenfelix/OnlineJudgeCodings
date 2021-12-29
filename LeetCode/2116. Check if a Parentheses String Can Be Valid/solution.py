class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lo, hi = 0, 0
        for i, ch in enumerate(s):
            if ch == '(':
                lo += 1
                hi += 1
                if locked[i] == '0':
                    lo -= 2
                    
            else:
                lo -= 1
                hi -= 1
                if locked[i] == '0':
                    hi += 2
            if lo < 0:
                lo += 2

            # print(i,ch,lo,hi)
            if hi < 0:
                return False
        return lo == 0
            

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n%2:
            return False
        cnt = 0
        for i in range(n):
            ch = s[i]
            if ch == '(' or locked[i] == '0':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                return False
        cnt = 0
        for i in range(n)[::-1]:
            ch = s[i]
            if ch == ')' or locked[i] == '0':
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                return False
        return True