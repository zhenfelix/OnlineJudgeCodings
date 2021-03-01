class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        mi_, mx_ = min(nums), max(nums)
        if mi_ == mx_:
            return 0
        sz = max(1,(mx_- mi_)//(n-1))
        # print(sz,n,mx_,mi_)
        N = (mx_- mi_)//sz + 1
        mi, mx =[float('inf')]*N, [-float('inf')]*N
        for x in nums:
            idx = (x-mi_)//sz
            mi[idx] = min(mi[idx],x)
            mx[idx] = max(mx[idx],x)
        res, pre = 0, mi_
        for i, cur in enumerate(mi):
            if cur == float('inf'):
                continue
            res = max(res, cur-pre)
            pre = mx[i]
        return res


# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         n, res = len(nums), 0
#         if n < 2:
#             return res
        
#         mx, mi = max(nums), min(nums)
#         d = max((mx-mi)//(n-1),1)
        
#         m = (mx-mi)//d + 1
#         lo, hi = [float('inf')]*m, [-float('inf')]*m 
#         for x in nums:
#             idx = (x-mi)//d
#             lo[idx] = min(lo[idx],x)
#             hi[idx] = max(hi[idx],x)
#         for i in range(1,m):
#             if lo[i] == float('inf'):
#                 hi[i] = hi[i-1]
#             else:
#                 if hi[i-1] > -float('inf'):
#                     res = max(res,lo[i]-hi[i-1])
#         return res 
