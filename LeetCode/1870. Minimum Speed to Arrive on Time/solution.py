class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        left, right = 1, 10**7
        while left <= right:
            mid = (left+right)//2
            cur = 0
            for d in dist:
                if cur > int(cur):
                    cur = int(cur)+1
                cur += d/mid 
            if cur <= hour:
                right = mid - 1
            else:
                left = mid + 1
        if left > 10**7:
            return -1
        return left