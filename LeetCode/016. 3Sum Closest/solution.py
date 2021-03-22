  
        
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        ans = [0]
        ans[0] = sum(nums[:3])
        def dfs(idx, N, t, result):
            if N == 2:
                left, right = idx, len(nums)-1
                while left < right:
                    if abs(nums[left]+nums[right]+result-target) < abs(ans[0]-target):
                        ans[0] = nums[left]+nums[right]+result
                        # print(result,nums[left],nums[right])
                        # left += 1
                        # right -= 1
                        # while left < right and nums[left] == nums[left-1]: left += 1
                        # while left < right and nums[right] == nums[right+1]: right -= 1
                        
                    if nums[left]+nums[right] > t:
                        right -= 1
                    else:
                        left += 1
                
                return
               
            for i in range(idx,len(nums)-N+1):
                # if t < nums[i]*N or t > nums[-1]*N:
                #     break
                if i == idx or nums[i] != nums[i-1]:
                    dfs(i+1, N-1, t-nums[i], result+nums[i])     
            return
        dfs(0,3,target,0)
        return ans[0]




class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = sum(nums[:3])
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            t = target-nums[i]
            left, right = i+1, n-1
            while left < right:
                if abs(nums[left]+nums[right]-t) < abs(res-target):
                    res = nums[i] + nums[left] + nums[right]
                if nums[left] + nums[right] > t:
                    right -= 1
                else:
                    left += 1
        return res
