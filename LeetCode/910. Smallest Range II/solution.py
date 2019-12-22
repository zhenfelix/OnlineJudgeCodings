class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1]-A[0]
        for i in range(len(A)-1):
            mx = max(A[-1],A[i]+2*K)
            mi = min(A[i+1],A[0]+2*K)
            # if mx-mi > res and A[i]!=A[i+1]:
            #     break
            res = min(res, mx-mi)
        return res