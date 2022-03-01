class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        return sum(w[:n]==pref for w in words)

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([1 for word in words if len(word) >= len(pref) and word[:len(pref)] == pref])


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/eU8bPl/view/rUilTq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。