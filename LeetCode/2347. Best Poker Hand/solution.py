class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return 'Flush'
        tmp = Counter(ranks)
        mx = max(tmp.values())
        if mx >= 3:
            return 'Three of a Kind'
        if mx == 2:
            return 'Pair'
        return 'High Card'


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/6jXNsy/view/fAD43m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        suits.sort()
        ranks.sort()
        if suits[0] == suits[-1]:
            return "Flush"
        for i in range(2,5):
            if ranks[i] == ranks[i-2]:
                return "Three of a Kind"
        for i in range(1,5):
            if ranks[i] == ranks[i-1]:
                return "Pair"
        return "High Card"