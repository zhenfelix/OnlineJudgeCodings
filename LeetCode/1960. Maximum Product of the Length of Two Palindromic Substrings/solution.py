class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        radius = [1]*n 
        left, right = 0, -1
        for i in range(n):
            if i <= right:
                radius[i] = min(radius[left+right-i], right-i+1)
            while i-radius[i] >= 0 and i+radius[i] < n and s[i-radius[i]] == s[i+radius[i]]:
                radius[i] += 1
            if i+radius[i]-1 > right:
                right = i+radius[i]-1
                left = i-radius[i]+1
        pre, suff = [1]*n, [1]*n 
        for i in range(n):
            j = i+radius[i]-1
            pre[j] = max(pre[j], radius[i]*2-1)
            j = i-radius[i]+1
            suff[j] = max(suff[j], radius[i]*2-1)
        for i in range(1,n):
            pre[i] = max(pre[i], pre[i-1])
        for i in range(n-1)[::-1]:
            pre[i] = max(pre[i], pre[i+1]-2)
        for i in range(n-1)[::-1]:
            suff[i] = max(suff[i], suff[i+1])
        for i in range(1,n):
            suff[i] = max(suff[i], suff[i-1]-2)
        return max(pre[i-1]*suff[i] for i in range(1,n))



