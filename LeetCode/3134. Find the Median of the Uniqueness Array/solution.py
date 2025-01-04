class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        def check(t):
            cnt = 0
            j = 0
            cc = Counter()
            uniq = 0
            for i in range(n):
                if cc[nums[i]] == 0: uniq += 1
                cc[nums[i]] += 1
                while uniq > t:
                    cc[nums[j]] -= 1
                    if cc[nums[j]] == 0: uniq -= 1
                    j += 1
                cnt += i-j+1
            return cnt

        lo, hi = 1, n  
        while lo <= hi:
            m = (lo+hi)//2
            # print(nums,m,check(m))
            if check(m) >= (n*(n+1)//2+1)//2:
                hi = m-1
            else:
                lo = m+1
        return lo  