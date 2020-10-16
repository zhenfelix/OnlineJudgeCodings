class Solution:
    # def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
    #     nums = [0] + nums
    #     n = len(nums)
    #     for i in range(1,n):
    #         nums[i] += nums[i-1]
    #     tmp = [0]*n 

    #     def merge(left,right):
    #         if left == right:
    #             return 0
    #         cnt, mid = 0, (left+right)//2
    #         cnt += merge(left,mid)
    #         cnt += merge(mid+1,right)
    #         j, k, p, q = mid+1, left, mid+1, mid+1
    #         for i in range(left,mid+1):
    #             while p <= right and nums[p]-nums[i] < lower:
    #                 p += 1
    #             while q <= right and nums[q]-nums[i] <= upper:
    #                 q += 1
    #             cnt += q-p
    #             while j <= right and nums[j] < nums[i]:
    #                 tmp[k] = nums[j]
    #                 k += 1
    #                 j += 1
    #             tmp[k] = nums[i]
    #             k += 1
    #             i += 1
    #         nums[left:right+1] = tmp[left:right+1]
    #         return cnt

    #     return merge(0,n-1)


    def countRangeSum(self, nums, lower, upper):
        n = len(nums)
        Sum, BITree = [0] * (n + 1), [0] * (n + 2)
        
        def count(x):
            s = 0
            while x:
                s += BITree[x]
                x -= (x & -x)
            return s
        
        def update(x):
            while x <= n + 1:
                BITree[x] += 1
                x += (x & -x)
                
        for i in range(n):
            Sum[i + 1] = Sum[i] + nums[i]
        sortSum, res = sorted(Sum), 0
        for sum_j in Sum:
            sum_i_count = count(bisect.bisect_right(sortSum, sum_j - lower)) - count(bisect.bisect_left(sortSum, sum_j - upper))
            res += sum_i_count
            update(bisect.bisect_left(sortSum, sum_j) + 1)
        return res






class SegNode:
    def __init__(self,mi,mx):
        self.cnt, self.mi, self.mx = 0, mi, mx
        self.left, self.right = None, None

class Solution:
    def buildTree(self,lo,hi,arr):
        root = SegNode(arr[lo],arr[hi])
        if lo < hi:
            mid = (lo+hi)//2
            root.left = self.buildTree(lo,mid,arr)
            root.right = self.buildTree(mid+1,hi,arr)
        return root

    def count(self,mi,mx,cur):
        if not cur or mx < cur.mi or mi > cur.mx:
            return 0
        if mx >= cur.mx and mi <= cur.mi:
            return cur.cnt 
        return self.count(mi,mx,cur.left) + self.count(mi,mx,cur.right)

    def update(self,val,cur):
        if not cur or val < cur.mi or val > cur.mx:
            return
        cur.cnt += 1
        # if cur.mi == cur.mx:
        #     return
        self.update(val,cur.left)
        self.update(val,cur.right)
        return

    def countRangeSum(self, nums, lower, upper):
        presums = [0] + nums
        n = len(presums)
        res = 0
        for i in range(1,n):
            presums[i] += presums[i-1]
        arr = sorted(set(presums))
        Root = self.buildTree(0,len(arr)-1,arr)
        for val in presums:
            res += self.count(val-upper,val-lower,Root)
            self.update(val,Root)
        
        return res