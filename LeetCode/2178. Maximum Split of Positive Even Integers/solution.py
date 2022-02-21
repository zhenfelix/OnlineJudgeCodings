class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2 != 0:
            return []
        res = []
        sums = finalSum//2
        cur = 1
        while sums-cur > cur:
            res.append(cur*2)
            sums -= cur
            cur += 1
        if sums > 0:
            res.append(sums*2)
        return res


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        ans = []
        now = 2
        while finalSum > 0:
            if finalSum < now:
                ans[-1] += finalSum
                finalSum = 0
            else:
                ans.append(now)
                finalSum -= now
                now += 2
        return ans


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/dinFl3/view/qn5Ww5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。