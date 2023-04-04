class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = pre = cur = 0
        for i, c in enumerate(s):
            cur += 1
            if i == len(s) - 1 or c != s[i + 1]:
                if c == '1':
                    ans = max(ans, min(pre, cur) * 2)
                pre = cur
                cur = 0
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/find-the-longest-balanced-substring-of-a-binary-string/solution/o1-kong-jian-jian-ji-xie-fa-pythonjavacg-u8g3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        st = [0]
        for i in range(1,n):
            if s[i] != s[i-1]: st.append(i)
            if s[i] == '1' and len(st) >= 2 and st[-1]-st[-2] >= i-st[-1]+1:
                ans = max(ans,(i-st[-1]+1)*2)
        return ans


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            j = i 
            zeros = ones = 0
            while j < n and s[j] == '0':
                j += 1
                zeros += 1  
            while j < n and s[j] == '1':
                j += 1
                ones += 1
                if ones == zeros:
                    ans = max(ans,2*zeros)
        return ans 