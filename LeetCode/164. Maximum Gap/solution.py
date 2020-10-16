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
