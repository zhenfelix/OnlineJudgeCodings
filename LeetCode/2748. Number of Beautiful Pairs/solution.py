class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            a = str(nums[i])
            for j in range(i+1,n):
                b = str(nums[j])
                if gcd(int(a[0]),int(b[-1])) == 1:
                    ans += 1
        return ans 