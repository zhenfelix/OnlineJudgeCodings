class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        cc = Counter()
        def convert(a,b):
            g = gcd(a,b)
            return (a//g,b//g)
        for r in range(3,n):
            for s in range(r+2,n):
                cc[convert(nums[s],nums[r])] += 1
        ans = 0
        for q in range(2,n-4):
            r = q+1
            for s in range(r+2,n):
                cc[convert(nums[s],nums[r])] -= 1 
            for p in range(0,q-1):
                ans += cc[convert(nums[p],nums[q])]
        return ans 



import math
def get(x, y):
    val = math.gcd(x,y)
    return (x//val, y//val)

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        assert 7 <= len(nums) <= 1000
        for i in nums:
            assert 1 <= i <= 1000 

        fdict = defaultdict(int) 
        n = len(nums)
        res = 0
        for j in range(n):
            for k in range(j+2, n):
                res += fdict[get(nums[k], nums[j])]
            for i in range(0,j-2):
                fdict[get(nums[i], nums[j-1])] += 1 
        return res 

            
            
                