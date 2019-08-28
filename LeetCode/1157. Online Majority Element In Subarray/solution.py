# [C++] Codes of different approaches (Random Pick, Trade-off, Segment Tree, Bucket)
# https://leetcode.com/problems/online-majority-element-in-subarray/discuss/356227/C++-Codes-of-different-approaches-(Random-Pick-Trade-off-Segment-Tree-Bucket)

# import random

# class MajorityChecker:

#     def __init__(self, arr: List[int]):
#         self.mp = {}
#         self.arr = arr
#         for i, a in enumerate(arr):
#             if a not in self.mp:
#                 self.mp[a] = []
#             self.mp[a] += [i]

#     def query(self, left: int, right: int, threshold: int) -> int:
#         try_count = 10
#         for i in range(try_count):
#             idx = random.randint(left,right)
#             a = self.arr[idx]
#             l = self.lower_bound(self.mp[a], left)
#             r = self.upper_bound(self.mp[a], right)
#             if r-l+1 >= threshold:
#                 return a
#         return -1
    
    
#     def lower_bound(self, nums, target):
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = (left+right)//2
#             if nums[mid] >= target:
#                 right = mid-1
#             else:
#                 left = mid+1
#         return right+1
    
#     def upper_bound(self, nums, target):
#         left, right = 0, len(nums)-1
#         while left <= right:
#             mid = (left+right)//2
#             if nums[mid] <= target:
#                 left = mid+1
#             else:
#                 right = mid-1
#         return left-1
        
    
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.mp = {}
        self.arr = arr
        self.tree = [-1]*(len(arr)*4)
        for i, a in enumerate(arr):
            if a not in self.mp:
                self.mp[a] = []
            self.mp[a] += [i]
        self._build(0,len(arr)-1,0)
        # print(self.tree)
        return
            
    def _build(self, low, high, pos):
        if low == high:
            self.tree[pos] = self.arr[low]
            return
        mid = (low+high)//2
        self._build(low,mid,pos*2+1)
        self._build(mid+1,high,pos*2+2)
        if self.tree[pos*2+1] != -1 and self._get_occurence(low,high,self.tree[pos*2+1])*2 > high-low+1:
            self.tree[pos] = self.tree[pos*2+1]
            return
        elif self.tree[pos*2+2] != -1 and self._get_occurence(low,high,self.tree[pos*2+2])*2 > high-low+1:
            self.tree[pos] = self.tree[pos*2+2]
            return
        self.tree[pos] = -1
        return 
        

    def query(self, left: int, right: int, threshold: int) -> int:
        return self._query(0,len(self.arr)-1,0,left,right,threshold)
        
    def _query(self, low, high, pos, left, right, threshold):
        if low >= left and high <= right:
            if self.tree[pos] != -1:
                cc = self._get_occurence(left,right,self.tree[pos])
                if cc >= threshold:
                    return self.tree[pos]
            return -1
        elif high < left or low > right:
            return -1
        else:
            mid = (low+high)//2
            ans = self._query(low,mid,pos*2+1,left,right,threshold)
            if ans != -1:
                return ans
            ans = self._query(mid+1,high,pos*2+2,left,right,threshold)
            if ans != -1:
                return ans
            return -1
        
    
    def _get_occurence(self, low, high, val):
        l = self.lower_bound(self.mp[val], low)
        r = self.upper_bound(self.mp[val], high)
        return r-l+1
    
    def lower_bound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid-1
            else:
                left = mid+1
        return right+1
    
    def upper_bound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1
        return left-1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)