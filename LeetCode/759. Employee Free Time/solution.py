
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

def __str__(self):
    return '['+str(self.start)+','+str(self.end)+']'

class Solution:
    def __init__(self):
        Interval.__repr__ = __str__
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        nums = []
        ans = []
        n = len(schedule)
        for arr in schedule:
            for a in arr:
                nums.append((a.start+1,-1))
                nums.append((a.end,1))
        nums.sort()
        cnt = n 
        pre = -float('inf')
        for cur, delta in nums:
            # print(cur,delta,cnt,pre,cur)
            if cnt == n and cur-1 > pre and pre > -float('inf'):
                ans.append(Interval(pre,cur-1))
            cnt += delta
            pre = cur
        return ans


"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

def __str__(self):
    return '['+str(self.start)+','+str(self.end)+']'

class Solution:
    def __init__(self):
        Interval.__repr__ = __str__
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        def overlap(a, b):
            s = max(a.start, b.start)
            e = min(a.end, b.end)
            if s < e:
                return True, Interval(s,e)
            return False, None

        dp = [Interval(-float('inf'), float('inf'))]
        for arr in schedule:
            rarr = []
            pre = -float('inf')
            for a in arr:
                s, e = a.start, a.end
                rarr.append(Interval(pre,s))
                pre = e
            rarr.append(Interval(pre,float('inf')))
            ndp = []
            # print(rarr, dp)
            for a in rarr:
                for b in dp:
                    flag, c = overlap(a,b)
                    if flag:
                        ndp.append(c)
            dp = ndp
        i, j = 0, len(dp)-1
        if dp[i].start == -float('inf'):
            i += 1
        if dp[j].end == float('inf'):
            j -= 1
        return dp[i:j+1]