class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        seen = set(forbidden)
        n = len(word)
        flag = [n]*n 
        m = 10
        for i in range(n):
            if flag[i] == 0: continue
            for j in range(i,min(n,i+m)):
                if word[i:j+1] in seen:
                    flag[i] = j
                    break
        ans = 0
        hq = []
        j = n-1
        for i in range(n)[::-1]:
            heappush(hq,flag[i])
            while hq and hq[0] <= j:
                j -= 1
            ans = max(ans,j-i+1)
        return ans 


class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        fb = set(forbidden)
        ans = left = 0
        for right in range(len(word)):
            for i in range(right, max(right - 10, left - 1), -1):
                if word[i: right + 1] in fb:
                    left = i + 1  # 当子串右端点 >= right 时，合法子串一定不能包含 word[i]
                    break
            ans = max(ans, right - left + 1)
        return ans


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/circle/discuss/FGLo5F/view/Oelnvj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。