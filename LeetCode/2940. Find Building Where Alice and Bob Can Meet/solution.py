# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/solutions/4304269/java-c-python-priority-queue/
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def ignore(i,j):
            return i == j or heights[i] < heights[j]
        n, m = len(heights), len(queries)
        ans = [-1]*m 
        candidates = [[] for _ in range(n)]
        for i, (l,r) in enumerate(queries):
            if l > r: l, r = r, l  
            if ignore(l,r):
                ans[i] = r 
            else:
                candidates[r].append((max(heights[l],heights[r]),i))
        hq = []
        for r, h in enumerate(heights):
            while hq and hq[0][0] < h:
                ans[hq[0][-1]] = r 
                heappop(hq)
            for hx, i in candidates[r]:
                heappush(hq,(hx,i))
        return ans 

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        m = len(queries)
        idx = list(range(m))
        idx.sort(key = lambda x: -max(queries[x]))
        ans = [-1]*m 
        j = n-1
        st = []
        for i in idx:
            l, r = queries[i]
            if l > r : l, r = r, l 
            if l == r: 
                ans[i] = l
                continue
            while j >= r:
                while st and heights[st[-1]] < heights[j]:
                    st.pop()
                st.append(j)
                j -= 1
            lo, hi = 0, len(st)-1
            while lo <= hi:
                t = (lo+hi)//2
                if heights[st[t]] > heights[l]:
                    lo = t+1
                else:
                    hi = t-1
            if hi >= 0:
                ans[i] = st[hi]
        return ans 

# 在线查询+st表+二分
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n, m = len(heights), len(queries)
        ans = [-1]*m 
        sz = 0
        while (1<<sz) <= n:
            sz += 1
        st = [[0]*sz for _ in range(n)]
        for i in range(n): st[i][0] = heights[i]
        for j in range(1,sz):
            for i in range(n):
                if i+(1<<j) > n: break 
                st[i][j] = max(st[i][j-1],st[i+(1<<(j-1))][j-1])
        log2 = [0]*n 
        j = 0
        for i in range(1,n):
            if (1<<(j+1)) < i+1: j += 1
            log2[i] = j 
        # print(st)
        # print(log2)
        def query(l,r):
            j = log2[r-l+1]
            d = 1<<j
            return max(st[l][j],st[r-d+1][j])
        for i, (l, r) in enumerate(queries):
            # print("query",i,l,r)
            if l > r: l, r = r, l 
            if l == r or heights[l] < heights[r]:
                ans[i] = r 
                continue
            lo, hi = r, n-1
            while lo <= hi:
                t = (lo+hi)//2
                # print(r,t,query(r,t))
                if query(r,t) > heights[l]:
                    hi = t-1
                else:
                    lo = t+1
            if lo < n:
                ans[i] = lo 
        return ans 