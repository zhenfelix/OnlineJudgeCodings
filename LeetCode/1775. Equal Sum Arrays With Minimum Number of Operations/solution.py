class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        delta = s2 - s1
        if delta < 0:
            nums1, nums2 = nums2, nums1
            delta = -delta
        cnt = 0
        heapq.heapify(nums1)
        nums2 = [-x for x in nums2]
        heapq.heapify(nums2)
        while delta > 0:
            diff = min(delta,5)
            diff1, diff2 = 6-nums1[0], -1-nums2[0]
            if diff1 <= 0 and diff2 <= 0:
                return -1
            if diff1 > diff2:
                diff = min(diff,diff1)
                delta -= diff 
                heapq.heappush(nums1,heapq.heappop(nums1)+diff)
            else:
                diff = min(diff,diff2)
                delta -= diff
                heapq.heappush(nums2,heapq.heappop(nums2)+diff)
            cnt += 1
        return cnt