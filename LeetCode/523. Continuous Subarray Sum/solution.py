class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        mp = {0: [-1]}
        k = abs(k)
        for i, num in enumerate(nums):
            if i > 0:
                nums[i] += nums[i-1]
            if k > 0:
                nums[i] %= k
            if nums[i] not in mp:
                mp[nums[i]] = [i]
            else:
                if i - mp[nums[i]][0] > 1:
                    return True
                mp[nums[i]] += [i]
        return False
        