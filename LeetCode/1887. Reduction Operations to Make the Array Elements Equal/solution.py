class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cc = Counter(nums)
        arr = [(k,v) for k, v in cc.items()]
        arr.sort(reverse = True)
        arr = [v for k, v in arr]
        n = len(arr)
        res, cur = 0, 0
        for i in range(n-1):
            cur += arr[i]
            res += cur
        return res 


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = val = 0
        nums.sort()
        for i in range(1, len(nums)): 
            if nums[i-1] < nums[i]: val += 1
            ans += val
        return ans 