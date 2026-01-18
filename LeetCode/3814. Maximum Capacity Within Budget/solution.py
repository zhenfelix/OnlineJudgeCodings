class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        arr = sorted(zip(costs, capacity))
        n = len(arr)
        pre = [0] * n
        mx = ans = 0
        
        for i, (c, cap) in enumerate(arr):
            mx = max(mx, cap)
            pre[i] = mx
            if c < budget: ans = max(ans, cap)
            
        j = 0
        for i in range(n - 1, 0, -1):
            while j < n and arr[j][0] + arr[i][0] < budget:
                j += 1
            idx = min(j - 1, i - 1)
            if idx >= 0:
                ans = max(ans, arr[i][1] + pre[idx])
                
        return ans