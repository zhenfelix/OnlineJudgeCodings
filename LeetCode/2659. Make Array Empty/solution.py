class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        n = len(nums)
        idx = sorted([i for i in range(n)], key = lambda x : nums[x])
        cnt = [0]*(n+5)
        def query(x):
            cur = 0
            while x:
                cur += cnt[x]
                x -= (x&-x)
            return cur 
        def update(x, delta):
            while x <= n:
                cnt[x] += delta
                x += (x&-x)
            return  
        ans = 0
        p = -1
        for i in range(n):
            update(i+1,1)
        for i in idx:
            if p > i:
                ans += query(i+1)+query(n)-query(p+1)
            else:
                ans += query(i+1)-query(p+1)
            update(i+1,-1)
            p = i  
        return ans 