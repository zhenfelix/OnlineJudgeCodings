class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cc1 = Counter(word1)
        cc2 = Counter(word2)
        cnt1 = [cc1[chr(ord('a')+ch)] for ch in range(26)]
        cnt2 = [cc2[chr(ord('a')+ch)] for ch in range(26)]
        return all(abs(x-y) <= 3 for x, y in zip(cnt1,cnt2))

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1 = collections.Counter(word1)
        cnt2 = collections.Counter(word2)
        return all(abs(cnt1[key] - cnt2[key]) <= 3 for key in set(cnt1.keys()) | set(cnt2.keys()))


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/cj4dO9/view/Mwspom/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。