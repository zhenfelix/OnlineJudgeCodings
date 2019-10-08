from collections import deque

class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        def great(x):
            if len(x) == len(low):
                return x >= low
            return len(x) > len(low)
        def less(x):
            if len(x) == len(high):
                return x <= high
            return len(x) < len(high)
        def isValid(x):
            return len(x) == 1 or x[0] != '0'

        q = deque(['0','1','8','00','11','69','88','96'])
        chrs = ['00','11','69','88','96']
        ans = 0
        while q:
            front = q.popleft()
            if less(front):
                if isValid(front) and great(front):
                    # print(front)
                    ans += 1
                for ch in chrs:
                    q.append(ch[0]+front+ch[-1])
        return ans