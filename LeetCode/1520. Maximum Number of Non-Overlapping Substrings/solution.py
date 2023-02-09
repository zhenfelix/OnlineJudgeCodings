class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        start, end = {}, {}
        for i, ch in enumerate(s):
            if ch not in start:
                start[ch] = i 
            end[ch] = i
        intervals = []
        for ch in start.keys():
            l, r = start[ch], end[ch] 
            q = list(s[l:r+1])
            while q:
                nq = []
                q = list(set(q))
                for cur in q:
                    if start[cur] < l:
                        for nxt in s[start[cur]:l]:
                            nq.append(nxt)
                        l = start[cur]
                    if end[cur] > r:
                        for nxt in s[r+1:end[cur]+1]:
                            nq.append(nxt)
                        r = end[cur]
                q = nq 
            intervals.append((l,r))
        ans = []
        pre = -1
        intervals.sort(key = lambda x: (x[-1], -x[0]))
        for l, r in intervals:
            if l > pre:
                ans.append(s[l:r+1])
                pre = r 
        return ans


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        start, end = {}, {}
        for i, ch in enumerate(s):
            if ch not in start:
                start[ch] = i 
            end[ch] = i
        st, res = [], []
        for i, ch in enumerate(s):
            if start[ch] == i:
                st.append(i)
            if end[ch] == i and st:
                pre = s[st.pop()]
                
                for k in range(start[pre],end[ch]+1):
                    if start[s[k]] < start[pre] or end[s[k]] > end[ch]:
                        break
                else:
                    res.append(s[start[pre]:end[ch]+1])
                    st = []
        return res



class Solution:
    def maxNumOfSubstrings(self, ss: str) -> List[str]:
        n = len(ss)
        left, right, cnt = [n]*26, [-1]*26, [0]*26 
        s = [ord(ch)-ord('a') for ch in ss]
        for i, ch in enumerate(s):
            left[ch] = min(left[ch],i)
            right[ch] = max(right[ch],i)
            cnt[ch] += 1
        intervals = []
        for ch in range(26):
            intervals.append((left[ch],right[ch]))
        ans = []
        
        m = len(intervals)
        sz = [r-l+1 for l, r in intervals]
        parent = list(range(m))
        def find(cur):
            if parent[cur] != cur:
                parent[cur] = find(parent[cur])
            return parent[cur]
        def connect(u,v):
            ru, rv = find(u), find(v)
            if ru != rv and sz[ru] != cnt[ru] and sz[rv] != cnt[rv]:
                parent[ru] = rv 
                leftu, rightu = intervals[ru]
                leftv, rightv = intervals[rv]
                intervals[rv] = (min(leftu,leftv),max(rightu,rightv))
                l, r = intervals[rv]
                sz[rv] = r-l+1
                cnt[rv] += cnt[ru]
            return
        idx = list(range(m))
        idx.sort(key = lambda x: intervals[x][-1]-intervals[x][0])
        # intervals.sort(key = lambda x: x[-1]-x[0])
        for i in range(m):
            l1,r1 = intervals[idx[i]]
            if l1 > r1: continue
            for ch in s[l1:r1+1]:
                l2,r2 = intervals[ch]
                if l2 > r2: continue
                if (r1 < l2) or (r2 < l1): continue
                connect(idx[i],ch)
                
        # print(sz)
        intervals = [(i,intervals[i][0],intervals[i][1]) for i in set([find(i) for i in range(m)])]
        ans = [(l,r) for i, l, r in intervals if cnt[i] == sz[i]]
        # print(ans,intervals)
       
        return [ss[l:r+1] for l,r in ans]