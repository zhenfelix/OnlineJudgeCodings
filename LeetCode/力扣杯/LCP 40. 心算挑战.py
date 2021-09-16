class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort()
        sums = sum(cards[-cnt:])
        if sums%2 == 0:
            return sums
        res = 0 
        hi_1, hi_0 = min([x for x in cards[-cnt:] if x%2 == 1], default = float('inf')), min([x for x in cards[-cnt:] if x%2 == 0], default = float('inf'))
        lo_1, lo_0 = max([x for x in cards[:-cnt] if x%2 == 1], default = float('inf')), max([x for x in cards[:-cnt] if x%2 == 0], default = float('inf'))
        if hi_1 != float('inf') and lo_0 != float('inf'):
            res = max(res, sums+lo_0-hi_1)
        if hi_0 != float('inf') and lo_1 != float('inf'):
            res = max(res, sums+lo_1-hi_0)
        return res 


class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards = sorted(cards, reverse=True)
        e1 = [t for t in cards[:cnt] if t % 2 == 0]
        o1 = [t for t in cards[:cnt] if t % 2 == 1]
        e2 = [t for t in cards[cnt:] if t % 2 == 0]
        o2 = [t for t in cards[cnt:] if t % 2 == 1]
        sumt = sum(e1+o1)
        if len(o1) % 2 == 0 :
            return sumt
        to_ret = 0
        if len(e2) > 0 :
            to_ret = max(to_ret, sumt+e2[0]-o1[-1])
        if len(o2) > 0 and len(e1) > 0 :
            to_ret = max(to_ret, sumt+o2[0]-e1[-1])
        return to_ret


作者：pku_erutan
链接：https://leetcode-cn.com/circle/discuss/jLMlw8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。