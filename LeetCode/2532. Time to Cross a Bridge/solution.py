class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        idx = list(range(k))
        idx.sort(key = lambda x: (-time[x][0]-time[x][2],-x))
        time = [time[t] for t in idx]
        left, right = [(0,i) for i in range(k)], []
        heapify(left)
        ready = []
        cur = end = 0
        while left or right or ready:
            while left and left[0][0] <= cur:
                heappush(ready, (1,heappop(left)[-1]))
            while right and right[0][0] <= cur:
                heappush(ready, (-1,heappop(right)[-1]))
            if not ready:
                cur = min(left[0][0] if left else inf, right[0][0] if right else inf)
                continue
            flag, i = heappop(ready)
            if flag == 1:
                if n == 0:
                    continue
                leftToRight, pickOld, rightToLeft, putNew = time[i]
                cur += leftToRight
                heappush(right, (cur+pickOld,i))
                n -= 1
            else:
                leftToRight, pickOld, rightToLeft, putNew = time[i]
                cur += rightToLeft
                end = cur
                heappush(left, (cur+putNew,i))
        return end
