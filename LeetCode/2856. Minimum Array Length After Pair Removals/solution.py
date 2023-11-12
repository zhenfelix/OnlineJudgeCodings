class Solution:

    def minLengthAfterRemovals(self, nums: List[int]) -> int:

        n = len(nums)

        v = max(Counter(nums).values())

        return n % 2 if v * 2 <= n else n - (n - v) * 2

# 作者：小羊肖恩
# 链接：https://leetcode.cn/problems/minimum-array-length-after-pair-removals/solutions/2445477/xiao-yang-xiao-en-shu-xue-tan-xin-jie-ju-rr7s/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        cc = Counter(nums)
        hq = list(cc.values())
        hq = [-x for x in hq]
        heapify(hq)
        while len(hq) > 1:
            a = heappop(hq)
            b = heappop(hq)
            a += 1
            if a < 0: heappush(hq,a)
            b += 1
            if b < 0: heappush(hq,b)
        if hq: return -hq[0]
        return 0