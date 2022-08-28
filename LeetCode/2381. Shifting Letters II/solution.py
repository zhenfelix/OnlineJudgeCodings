class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0]*(n+1)
        for left, right, cnt in shifts:
            if cnt == 0:
                cnt = -1
            delta[left] += cnt
            delta[right+1] -= cnt
        cur = 0
        ans = []
        for i, ch in enumerate(s):
            cur += delta[i]
            cur %= 26
            ans.append(chr(ord('a')+(ord(ch)-ord('a')+cur)%26))
        return ''.join(ans)


c2i = {c: i for i, c in enumerate(ascii_lowercase)}

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for start, end, dir in shifts:
            diff[start] += dir * 2 - 1
            diff[end + 1] -= dir * 2 - 1
        return ''.join(ascii_lowercase[(c2i[c] + shift) % 26] for c, shift in zip(s, accumulate(diff)))


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/shifting-letters-ii/solution/by-endlesscheng-z0ad/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。