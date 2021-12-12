class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cc1, cc2 = Counter(words1), Counter(words2)
        return sum(cc1[w] == 1 and cc2[w] == 1 for w in words1)


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = collections.Counter(words1)
        c2 = collections.Counter(words2)
        return len([key for key in c1 if c1[key] == 1 and c2[key] == 1])


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/jPIdc4/view/8u6s2V/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。