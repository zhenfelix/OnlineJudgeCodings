# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:

        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        def dfs(idx, N, t, result):
            if N == 2:
                left, right = idx, len(nums)-1
                while left < right:
                    if nums[left]+nums[right] == t:
                        results.append(result+[nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]: left += 1
                        while left < right and nums[right] == nums[right+1]: right -= 1
                        
                    elif nums[left]+nums[right] > t:
                        right -= 1
                    else:
                        left += 1
                
                return
               
            for i in range(idx,len(nums)-N+1):
                if t < nums[i]*N or t > nums[-1]*N:
                    break
                if i == idx or nums[i] != nums[i-1]:
                    dfs(i+1, N-1, t-nums[i], result+[nums[i]])     
            return
        dfs(0,3,0,[])
        return results
                    
            