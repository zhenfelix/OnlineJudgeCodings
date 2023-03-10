class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        nums = []
        for i, v in nums1:
            nums.append((i,v))
        for i, v in nums2:
            nums.append((i,v))
        ans = []
        for i, v in sorted(nums):
            if ans and ans[-1][0] == i:
                ans[-1][-1] += v  
            else:
                ans.append([i,v])
        return ans 