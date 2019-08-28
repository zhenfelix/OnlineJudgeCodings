class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        ans = sums
        end = k
        while end < len(nums):
            sums += nums[end]
            sums -= nums[end-k]
            ans = max(ans, sums)
            end += 1
            
        return ans/k