class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        left1 = bisect.bisect_left(nums1, 0)
        right1 = bisect.bisect_right(nums1, 0)
        left2 = bisect.bisect_left(nums2, 0)
        right2 = bisect.bisect_right(nums2, 0)
        # print(left1,right1,left2,right2)

        def leq(target):
            cnt = 0
            i, j = 0, right1
            while i < left2 and j < n1:
                if nums2[i]*nums1[j] <= target:
                    i += 1
                    cnt += n1-j
                else:
                    j += 1
                    
            i, j = right2, 0
            while i < n2 and j < left1:
                if nums2[i]*nums1[j] <= target:
                    j += 1
                    cnt += n2-i
                else:
                    i += 1
                    
            if target < 0:
                return cnt
            cnt += (right1-left1)*n2+(right2-left2)*n1-(right1-left1)*(right2-left2)
            if target == 0:
                return cnt
            i, j = right2, n1-1
            while i < n2 and j >= right1:
                if nums2[i]*nums1[j] <= target:
                    i += 1
                    cnt += j-right1+1
                else:
                    j -= 1
                    
            i, j = 0, left1-1
            while i < left2 and j >= 0:
                if nums2[i]*nums1[j] <= target:
                    j -= 1
                    cnt += left2-i
                else:
                    i += 1
            return cnt
                    




        lo, hi = -10**10, 10**10
        while lo <= hi:
            mid = (lo+hi)//2
            # print(lo,hi,mid,leq(mid))
            if leq(mid) >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

