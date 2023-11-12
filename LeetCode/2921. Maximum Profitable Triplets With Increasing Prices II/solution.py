class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        mx = 5005
        tree = [0]*mx 
        n = len(prices)
        def query(i):
            ans = 0
            while i:
                ans = max(ans,tree[i])
                i -= i&-i
            return ans 
        def update(i,v):
            while i < mx:
                tree[i] = max(tree[i], v)
                i += i&-i 
            return
        left = [0]*n 
        right = [0]*n 
        for i in range(n):
            p = prices[i]
            left[i] = query(p-1)
            update(p,profits[i])
        tree = [0]*mx 
        for i in range(n)[::-1]:
            p = mx-1-prices[i]
            right[i] = query(p-1)
            update(p,profits[i])
        # print(left,right)
        ans = 0
        for i in range(1,n-1):
            if left[i] and right[i]:
                ans = max(ans,left[i]+right[i]+profits[i])
        return ans if ans else -1