class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        right = [0] * 3
        for i, s in enumerate(garbage):
            ans += len(s)
            for j, c in enumerate("MPG"):
                if c in s:
                    right[j] = i
        return ans + sum(sum(travel[:r]) for r in right)


作者：endlesscheng
链接：https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/solution/by-endlesscheng-bxks/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        reach = Counter()
        cc = Counter()
        for i, s in enumerate(garbage):
            cnt = Counter()
            for ch in s:
                cnt[ch] += 1
            for ch in ['P','G','M']:
                if cnt[ch] > 0:
                    reach[ch] = i
                    cc[ch] += cnt[ch]
        ans = 0
        presums = [0]
        for t in travel:
            presums.append(presums[-1]+t)
        for ch in ['P','G','M']:
            ans += cc[ch]
            ans += presums[reach[ch]]
        return ans 