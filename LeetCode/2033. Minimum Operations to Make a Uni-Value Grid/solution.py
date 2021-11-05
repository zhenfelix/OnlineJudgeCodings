class Solution:
    def minOperations(self, grid: List[List[int]], b: int) -> int:
        arr = []
        for row in grid:
            for x in row:
                arr.append(x)
        mi = min(arr)
        nums = []
        for x in arr:
            if x > 1 and (x-mi)%b != 0:
                return -1
            nums.append((x-mi)//b)
        nums.sort()
        n = len(nums)
        res = sum(abs(x-nums[n//2]) for x in nums)
        return res