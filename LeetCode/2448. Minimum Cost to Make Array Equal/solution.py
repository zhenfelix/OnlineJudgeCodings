class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        mx = max(nums)
        a = [0]*(mx+1)
        l = r = 0
        left = right = 0
        for v, c in zip(nums, cost):
            a[v] += c 
            right += v*c
            r += c
        res = right 

        for cur in range(mx+1):
            l += a[cur]
            r -= a[cur]
            left += l 
            right -= r 
            res = min(res, left+right)
        return res 
        


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        mi, mx = min(nums), max(nums)
        cost_cc = Counter()
        ltot, rtot = 0, 0
        l, r = 0, 0
        for v, c in zip(nums, cost):
            cost_cc[v] += c 
            rtot += (v-mi)*c
            r += c
        res = tot = ltot+rtot
        arr = sorted(list(set(nums)))
        n = len(arr)
        for i in range(n-1):
            cur = arr[i]
            nxt = arr[i+1]
            l += cost_cc[cur]
            r -= cost_cc[cur]
            tot += (l-r)*(nxt-cur)
            res = min(res, tot)
        return res 
        