class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def gcd(x,y):
            if x < y:
                x, y = y, x
            if y == 0:
                return x
            return gcd(y, x%y)
        g = numsDivide[0]
        for h in numsDivide:
            g = gcd(g, h)
        cnt = 0
        heapq.heapify(nums)
        while nums:
            cur = heapq.heappop(nums)
            if cur > g:
                return -1
            if g%cur == 0:
                return cnt
            cnt += 1 
        return -1