class Solution:
    def largestVariance(self, s: str) -> int:
        alphas = [chr(ord('a')+i) for i in range(26)]
        ans = 0
       
        for mx in alphas:
            for mi in alphas:
                if mx == mi:
                    continue
                miv = 0
                miv2 = float('inf')
                cur = 0
                for i, ch in enumerate(s):
                    if ch == mx:
                        cur += 1
                    elif ch == mi:
                        cur -= 1
                        miv2 = miv
                        miv = min(miv, cur)
                    ans = max(ans, cur-miv2)
        return ans



class Solution:
    def largestVariance(self, s: str) -> int:
        if s.count(s[0]) == len(s):
            return 0
        ans = 0
        for a in ascii_lowercase:
            for b in ascii_lowercase:
                if b == a:
                    continue
                diff, diff_with_b = 0, -inf
                for ch in s:
                    if ch == a:
                        diff += 1
                        diff_with_b += 1
                    elif ch == b:
                        diff -= 1
                        diff_with_b = diff  # 记录包含 b 时的 diff
                        if diff < 0:
                            diff = 0
                    if diff_with_b > ans:
                        ans = diff_with_b
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/substring-with-largest-variance/solution/by-endlesscheng-5775/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def largestVariance(self, s: str) -> int:
        if s.count(s[0]) == len(s):
            return 0
        ans = 0
        diff = [[0] * 26 for _ in range(26)]
        diff_with_b = [[-inf] * 26 for _ in range(26)]
        for ch in s:
            ch = ord(ch) - ord('a')
            for i in range(26):
                if i == ch:
                    continue
                diff[ch][i] += 1  # a=ch, b=i
                diff_with_b[ch][i] += 1
                diff[i][ch] -= 1  # a=i, b=ch
                diff_with_b[i][ch] = diff[i][ch]
                if diff[i][ch] < 0:
                    diff[i][ch] = 0
                ans = max(ans, diff_with_b[ch][i], diff_with_b[i][ch])
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/substring-with-largest-variance/solution/by-endlesscheng-5775/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。