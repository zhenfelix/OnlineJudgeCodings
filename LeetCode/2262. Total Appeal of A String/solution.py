class Solution:
    def appealSum(self, s: str) -> int:
        mp = dict()
        pre, tot = 0, 0
        for i, ch in enumerate(s):
            if ch not in mp:
                pre += i+1
                tot += pre
            else:
                pre += i-mp[ch]
                tot += pre 
            mp[ch] = i 
        return tot


class Solution:
    def appealSum(self, s: str) -> int:
        ans, sum_g, pos = 0, 0, [-1] * 26
        for i, c in enumerate(s):
            c = ord(c) - ord('a')
            sum_g += i - pos[c]
            ans += sum_g
            pos[c] = i
        return ans


# 作者：endlesscheng
# 链接：https://leetcode-cn.com/problems/total-appeal-of-a-string/solution/by-endlesscheng-g405/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。