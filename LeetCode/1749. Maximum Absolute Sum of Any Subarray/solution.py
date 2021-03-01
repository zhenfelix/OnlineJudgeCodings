class Solution:
    def maxAbsoluteSum(self, A):
        return max(accumulate(A, initial=0)) - min(accumulate(A, initial=0))        

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur, res = 0, 0
        miq, mxq = [cur], [cur]
        for x in nums:
            cur += x
            res = max(res, abs(cur-miq[0]))
            res = max(res, abs(cur+mxq[0]))
            heapq.heappush(miq, cur)
            heapq.heappush(mxq, -cur)
        return res  