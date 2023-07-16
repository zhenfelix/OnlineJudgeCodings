class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        delta = [0]*n 
        cur = 0
        for i in range(n):
            cur += delta[i]
            nums[i] += cur 
            if nums[i] < 0:
                return False
            if i+k-1 < n:
                cur -= nums[i]
                if i+k < n:
                    delta[i+k] += nums[i]
                nums[i] = 0
            if nums[i] != 0:
                return False
        return True