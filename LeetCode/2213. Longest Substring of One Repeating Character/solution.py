from sortedcontainers import SortedList
class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        sz = [1]*n 
        sl = defaultdict(SortedList)
        for i in range(n-1)[::-1]:
            if s[i] == s[i+1]:
                sz[i] += sz[i+1]
        pq = []
        for i in range(n):
            if i == 0 or s[i] != s[i-1]:
                sl[s[i]].add(i)
                heapq.heappush(pq, (-sz[i],i))
            else:
                sz[i] = -1
        # print(pq)
        # print(sl)
        # print(sz)
        k = len(queryIndices)
        ans = [-1]*k
        for i in range(k):
            ch, idx = queryCharacters[i], queryIndices[i]
            if idx > 0 and s[idx-1] == s[idx]:
                root = sl[s[idx]][sl[s[idx]].bisect_right(idx)-1]
                w = sz[root]
                sz[root] = idx-root
                heapq.heappush(pq, (-sz[root],root))
                sz[idx] = w-sz[root]
                # sl[s[idx]].add(idx)
                # heapq.heappush(pq, (-sz[idx],idx))
            if idx+1 < n and s[idx+1] == s[idx]:
                sz[idx+1] = sz[idx]-1
                sl[s[idx]].add(idx+1)
                heapq.heappush(pq, (-sz[idx+1],idx+1))

            if sl[s[idx]].count(idx):
                sl[s[idx]].remove(idx)

            sz[idx] = 1
            s[idx] = ch
            # print(i,ch,s)
            sl[s[idx]].add(idx)
            
            if idx+1 < n and s[idx] == s[idx+1]:
                sz[idx] += sz[idx+1]
                heapq.heappush(pq,(-sz[idx],idx))
                sz[idx+1] = -1
                sl[s[idx]].remove(idx+1)            
            if idx-1 >= 0 and s[idx-1] == s[idx]:
                root = sl[s[idx]][sl[s[idx]].bisect_left(idx)-1]
                sz[root] += sz[idx]
                heapq.heappush(pq,(-sz[root],root))
                sz[idx] = -1
                sl[s[idx]].remove(idx)
            while -pq[0][0] != sz[pq[0][-1]]:
                heapq.heappop(pq)
            ans[i] = -pq[0][0]
            # print(pq)
            # print(sl)
            # print(sz)
        return ans
