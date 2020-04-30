# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         n, sums = len(cardPoints), sum(cardPoints)
#         presum = sum(cardPoints[:n-k])
#         res = presum
#         for i in range(n-k,n):
#             presum += cardPoints[i]-cardPoints[i-(n-k)]
#             res = min(res, presum)
#         return sums-res

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = k - 1
        j = len(cardPoints)-1
        ans = sum(cardPoints[:k])
        cur = ans
        while(i>=0):
            cur -= cardPoints[i]
            cur += cardPoints[j]
            i -= 1
            j -= 1
            ans = max(ans, cur)
        return ans