import bisect 

class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        c, r, h = 0, 0, 0
        for i, inc in enumerate(increase):
            c, r, h = inc[0]+c, inc[1]+r, inc[2]+h
            increase[i][0], increase[i][1], increase[i][2] = c, r, h
        increase = [[0,0,0]] + increase
        cs = list(map(lambda x:x[0], increase))
        rs = list(map(lambda x:x[1], increase))
        hs = list(map(lambda x:x[2], increase))
        ans = []
        for c,r,h in requirements:
            d = max(bisect.bisect_left(cs,c),bisect.bisect_left(rs,r),bisect.bisect_left(hs,h))
            if d >= len(increase):
                d = -1
            ans.append(d)
        return ans
