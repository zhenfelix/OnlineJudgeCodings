# class Solution:
#     def largestPalindrome(self, n: int, k: int) -> str:
#         arr = [1]*n 
#         for i in range(1,n):
#             arr[i] = (arr[i-1]*10)%k 
#         ans = ['']*n 

#         @lru_cache(None)
#         def dfs(i,j):
#             if i > n-1-i: return j == 0
#             for d in range(10)[::-1]:
#                 tmp = (d*arr[i]+j)%k if i == n-1-i else (d*(arr[i]+arr[n-1-i])+j)%k
#                 ans[i] = str(d)
#                 if i != n-1-i: ans[n-1-i] = str(d)
#                 if dfs(i+1,tmp): return True
#             return False

#         dfs(0,0)
#         return ''.join(ans)
class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        pow10 = [1] * n
        for i in range(1, n):
            pow10[i] = pow10[i - 1] * 10 % k

        ans = [''] * n
        m = (n + 1) // 2
        vis = [[False] * k for _ in range(m + 1)]
        def dfs(i: int, j: int) -> bool:
            if i == m:
                return j == 0
            vis[i][j] = True
            for d in range(9, -1, -1):  # 贪心：从大到小枚举
                if n % 2 and i == m - 1:  # 正中间
                    j2 = (j + d * pow10[i]) % k
                else:
                    j2 = (j + d * (pow10[i] + pow10[-1 - i])) % k
                if not vis[i + 1][j2] and dfs(i + 1, j2):
                    ans[i] = ans[-1 - i] = str(d)
                    return True
            return False
        dfs(0, 0)
        return ''.join(ans)

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-the-largest-palindrome-divisible-by-k/solutions/2884548/tong-yong-zuo-fa-jian-tu-dfsshu-chu-ju-t-m3pu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。