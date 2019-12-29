class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        dp = [-1]*n
        for i in range(n-1)[::-1]:
            dp[i] = max(arr[i+1],dp[i+1])
        return dp

class Solution:
    def replaceElements(self, A, mx = -1):
        for i in range(len(A) - 1, -1, -1):
            A[i], mx = mx, max(mx, A[i])
        return A