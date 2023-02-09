class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for x in strs:
            try:
                ans = max(ans, int(x))
            except:
                ans = max(ans, len(x))
        return ans


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/xgnLKJ/view/6zOtKO/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def func(s):
            if all(ch.isdigit() for ch in s):
                return int(s)
            return len(s)
        return max(map(func,strs))