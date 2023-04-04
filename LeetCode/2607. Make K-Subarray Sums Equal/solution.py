class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        sz = gcd(n,k)
        nums = [[] for _ in range(sz)]
        for i in range(n):
            nums[i%sz].append(arr[i])
        ans = 0
        for brr in nums:
            brr.sort()
            m = len(brr)
            mid = m//2
            for j in range(m):
                ans += abs(brr[mid]-brr[j])
        return ans 