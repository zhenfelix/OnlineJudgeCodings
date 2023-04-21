class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        ans = [-1,-1]
        n = len(divisors)
        divisors.sort()
        for i in range(n):
            cnt = sum(a%divisors[i] == 0 for a in nums)
            if cnt > ans[0]:
                ans = [cnt,divisors[i]]
        return ans[-1]