from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        mp = Counter()
        n = len(s)
        for ch in s:
            mp[ch] += 1
        arr = [[-a[1],a[0]] for a in mp.items()]
        heapq.heapify(arr)
        ans = ''
        idx = 0
        q = deque()
        for i in range(k):
            q.append(None)
            
        for i in range(n):
            if not arr:
                return ''
            tmp = heapq.heappop(arr)
            ans += tmp[1]
            tmp[0] += 1
            if tmp[0] < 0:
                q.append(tmp.copy())
            else:
                q.append(None)
            tmp = q.popleft()
            if tmp:
                heapq.heappush(arr, tmp.copy())

        return ans
