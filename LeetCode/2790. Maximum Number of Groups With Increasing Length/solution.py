class Solution:
    def maxIncreasingGroups(self, x: List[int]) -> int:
        x.sort()
        n = len(x)
        curr = 0
        ans = 0
        for v in x:
            curr += v
            if curr >= ans + 1:
                ans += 1
                curr -= ans
        return ans


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/1AqXeK/view/L7qGfY/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

脑筋急转弯。

数字本身是啥不重要，因此我们可以对数组进行任意的排列。

我们考虑从最小频率到最大频率枚举，能分成的组数会怎么变化。

如果到某一个时刻，已经分成了 kk 组，还剩下了 notenote 个数，那么新来的频率 xx 如果满足 x+note≥k+1x+note≥k+1，那么可以分为 k+1k+1 组（同时也只能分为 k+1k+1 组，因为多一个数最多多一组）。

    构造：前面的 kk 组剔除一个元素，再把 note+xnote+x 个数中的 kk 个分配过去重新构造（可以完成分配的说明类似于归纳的构造），最后把前面 kk 组找来的元素和新的一个元素构成一个新组。

同时按频率从小到大一定是更优的（可以思考下为啥）。

因此按照上述逻辑模拟即可

时间复杂度为 O(nlog⁡n)O(nlogn).

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/1AqXeK/view/L7qGfY/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。