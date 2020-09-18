class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        hi, lo, res = 0, n-1, n 
        while hi+1 < n and arr[hi] <= arr[hi+1]:
            hi +=1
        if hi == n-1:
            return 0
        while lo-1 >= 0 and arr[lo-1] <= arr[lo]:
            lo -= 1
        left, right = 0, lo 
        while left <= hi:
            while right <= n-1 and arr[left] > arr[right]:
                right += 1
            res = min(res, right-left-1)
            left += 1
        left, right = hi, n-1 
        while right >= lo:
            while left >= 0 and arr[left] > arr[right]:
                left -= 1
            res = min(res, right-left-1)
            right -= 1
        return res 