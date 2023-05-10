class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = ord('a')
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n - 1
        s[i] += 1  # 从最后一个字母开始
        while i < n:
            if s[i] == k:  # 超过范围
                if i == 0: return ""  # 无法进位
                # 进位
                s[i] = a
                i -= 1
                s[i] += 1
            elif i and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:
                s[i] += 1  # 如果 s[i] 和前面的字符形成回文串，就继续增加 s[i]
            else:
                i += 1  # 检查 s[i] 是否和后面的字符形成回文串
        return ''.join(map(chr, s))


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/solution/tan-xin-pythonjavacgo-by-endlesscheng-yix5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。