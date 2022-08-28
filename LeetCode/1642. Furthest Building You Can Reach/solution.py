class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        hq = []
        pre = float('inf')
        for i, cur in enumerate(heights):
            if cur > pre:
                heapq.heappush(hq,-(cur-pre))
                bricks -= (cur-pre)
                if bricks < 0:
                    if ladders <= 0:
                        return i-1
                    ladders -= 1
                    bricks -= heapq.heappop(hq)
            pre = cur 
        return n-1

class Solution:
    def furthestBuilding(self, A, bricks, ladders):
        heap = []
        for i in range(len(A) - 1):
            d = A[i + 1] - A[i]
            if d > 0:
                heapq.heappush(heap, d)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i
        return len(A) - 1        
    
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diff, n = [], len(heights)
        for i in range(n-1):
            delta = heights[i+1]-heights[i]
            if delta > 0:
                diff.append((delta,i,i+1))
        diff.sort()
        lo, hi = 0, n-1
        while lo <= hi:
            cur = (lo+hi)//2
            sums, cnt, flag = 0, 0, True
            for delta, _, reach in diff:
                if reach > cur:
                    continue
                if sums + delta <= bricks:
                    sums += delta
                elif cnt + 1 <= ladders:
                    cnt += 1
                else:
                    flag = False
                    break
            if flag:
                lo = cur + 1
            else:
                hi = cur - 1
        return hi