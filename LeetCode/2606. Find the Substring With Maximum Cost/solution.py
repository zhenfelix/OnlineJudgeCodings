class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mp = {ch: v for ch, v in zip(chars,vals)}
        for i,ch in enumerate(ascii_lowercase):
            if ch not in mp: mp[ch] = i+1
        cur, ans, mi = 0, 0, 0
        for ch in s:
            cur += mp[ch]
            ans = max(ans, cur-mi)
            mi = min(mi,cur)
        return ans 


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mapping = dict(zip(chars, vals))
        ans = f = 0
        for c in s:
            f = max(f, 0) + mapping.get(c, ord(c) - ord('a') + 1)
            ans = max(ans, f)
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/3Cqiwp/view/uIYhPw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。