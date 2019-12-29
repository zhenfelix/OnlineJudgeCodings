class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        lo, hi = 0, max(arr)
        while lo <= hi:
            mid =(lo+hi)//2
            res = sum(mid if a >= mid else a for a in arr)
            if res >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        if abs(sum(lo if a >= lo else a for a in arr)-target) >= abs(sum(hi if a >= hi else a for a in arr)-target):
            return hi
        # print(lo,hi)
        return lo

