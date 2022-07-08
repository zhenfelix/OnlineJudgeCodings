# 参考
# 2263. Make Array Non-decreasing or Non-increasing
class Solution:
    def buildBridge(self, num: int, wood: List[List[int]]) -> int:
        s, e = wood[0]
        left, right = [-s], [s]
        biasL, biasR = 0, 0
        pre = e-s
        ans = 0
        for s, e in wood[1:]:
            cur = e - s 
            # 平移前一个函数的坐标轴
            biasL -= cur
            biasR += pre
            lo, hi = -left[0], right[0]
            lo += biasL
            hi += biasR
            if s > hi:
                ans += s-hi
                heapq.heappushpop(right, s-biasR)
                heapq.heappush(right, s-biasR)
                heapq.heappush(left, -(hi-biasL))
            elif s < lo:
                ans += lo-s
                heapq.heappushpop(left, -(s-biasL))
                heapq.heappush(left, -(s-biasL))
                heapq.heappush(right, lo-biasR)
            else:
                heapq.heappush(right, s-biasR)
                heapq.heappush(left, -(s-biasL))
            pre = cur
        return ans