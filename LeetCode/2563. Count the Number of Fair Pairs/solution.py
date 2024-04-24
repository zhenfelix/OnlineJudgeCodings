class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        l, r = n-1, n-1 
        for i in range(n):
            while l >= 0 and nums[i]+nums[l] >= lower:
                l -= 1
            while r >= 0 and nums[i]+nums[r] > upper:
                r -= 1
            if l < r:
                ans += r-l
                if l < i <= r:
                    ans -= 1
        return ans//2


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        l = r = 0
        nums.sort()
        ans = tmp = 0
        for i in range(n)[::-1]:
            while l < n and nums[l]+nums[i] < lower:
                l += 1
            while r < n and nums[r]+nums[i] <= upper:
                r += 1
            print(i,l,r)
            ans += r-l
            tmp += (lower <= nums[i]*2 <= upper)
        return (ans-tmp)//2 
