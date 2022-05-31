
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        ans = [-1] * len(queries)
        base = 10 ** ((intLength - 1) // 2)
        for i, q in enumerate(queries):
            if q <= 9 * base:
                s = str(base + q - 1)  # 回文数左半部分
                s += s[-2::-1] if intLength % 2 else s[::-1]
                ans[i] = int(s)
        return ans


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/find-palindrome-with-fixed-length/solution/fan-zhuan-hui-wen-shu-zuo-ban-bu-fen-by-4pvs0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        sz = (intLength+1)//2
        dp = [1]*(sz+1)
        dp[0] = 1
        for i in range(1,1+sz):
            dp[i] = 10*dp[i-1]
        n = len(queries)
        ans = [-1]*n 
        for i, q in enumerate(queries):
            sz = (intLength+1)//2
            s = [0]*sz
            for j in range(sz)[::-1]:
                cur = (q-1)//dp[j]
                s[j] = cur + (j==sz-1)
                q -= dp[j]*cur
            if 0 < s[-1] < 10:
                if intLength%2:
                    s = s[1:][::-1]+[s[0]]+s[1:]
                else:
                    s = s[::-1]+s
                # print(s)
                ans[i] = int(''.join(map(str,s)))
        return ans

