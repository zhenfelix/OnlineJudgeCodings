class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        n = len(A)
        left, right = 0, n-2
        while left+1 < right:
            mid = (left+right)//2
            if A[mid] < A[mid+1]:
                left = mid
            else:
                right = mid
        return right