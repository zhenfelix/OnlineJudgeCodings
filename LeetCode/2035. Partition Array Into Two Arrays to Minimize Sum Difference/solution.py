class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        tot = sum(nums)
        res = float('inf')
        for i in range(n//2+1):
            left = sorted(list(map(sum, combinations(nums[:n//2], i))))
            right = sorted(list(map(sum, combinations(nums[n//2:], n//2-i))))
            p, q = 0, len(right)-1
            while p < len(left) and q >= 0:
                sums = left[p]+right[q]
                res = min(res, abs(sums-(tot-sums)))
                if res == 0:
                    return 0
                if sums > tot/2:
                    q -= 1
                else:
                    p += 1
        return res

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//2
        tot = sum(nums)
        res = float('inf')
        for i in range(n+1):
            left = sorted(map(sum,combinations(nums[:n],i)))
            right = sorted(map(sum,combinations(nums[n:],n-i)))
            r = len(right)-1
            for l, x in enumerate(left):
                while r >= 0 and x+right[r] >= tot/2:
                    res = min(res, (x+right[r])*2-tot)
                    if res == 0:
                        return 0
                    r -= 1
        return res