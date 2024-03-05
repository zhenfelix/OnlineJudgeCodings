class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a = []
        for l, r in firstList:
            a.append((l,1))
            a.append((r+1,-1))
        b = []
        for l, r in secondList:
            b.append((l,1))
            b.append((r+1,-1))
        n, m = len(a), len(b)
        i, j = 0, 0 
        cur = 0
        ans = []
        while i < n and j < m:
            p = -1
            d = 0
            if a[i] <= b[j]:
                p = a[i][0]
                d = a[i][1]
                cur += d
                i += 1
            else:
                p = b[j][0]
                d = b[j][1]
                cur += d
                j += 1
            if cur == 2 and d == 1:
                ans.append([p])
            elif cur == 1 and d == -1:
                ans[-1].append(p-1)
        return ans 
        
