class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg, pos, res = [], [], []
        for x in nums:
            if x > 0:
                pos.append(x)
            else:
                neg.append(x)
        for a, b in zip(pos,neg):
            res.append(a)
            res.append(b)
        return res


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        return list(itertools.chain(*[[p, n] for p, n in zip(pos, neg)]))


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/S7rn0B/view/M2MJ7M/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。