# class Solution:
#     dp = {0: 0}
#     def minimumOneBitOperations(self, n):
#         if n not in self.dp:
#             b = 1
#             while (b << 1) <= n:
#                 b = b << 1
#             self.dp[n] = self.minimumOneBitOperations((b >> 1) ^ b ^ n) + 1 + b - 1
#         return self.dp[n]        

class Solution:
    def minimumOneBitOperations(self, n):
        ans = 0;
        while n:
            ans ^= n;
            n >>= 1;    
        return ans;

class Solution:
    def minimumOneBitOperations(self, n):
        mask = n
        while mask:
            mask >>= 1
            n ^= mask
              
        return n;


# grey code
# 九连环


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        idx = 0
        while (1<<idx) <= n:
            idx += 1
        def dfs(x, i):
            # print(x,i)
            if x <= 1:
                return x
            while (x>>i)&1 == 0:
                i -= 1
            return ((1<<(i+1))-1)-dfs(x-(1<<i),i)
        return dfs(n,idx)