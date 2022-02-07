from itertools import zip_longest
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds, even, res = [], [], []
        for i, x in enumerate(nums):
            if i&1:
                odds.append(x)
            else:
                even.append(x)
        odds.sort(reverse = True)
        even.sort()
        for u, v in zip_longest(even,odds):
            if u != None:
                res.append(u)
            if v != None:
                res.append(v)
        return res


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even = sorted([nums[i] for i in range(0, n, 2)])
        odd = sorted([nums[i] for i in range(1, n, 2)], reverse=True)
        return [even[i // 2] if i % 2 == 0 else odd[i // 2] for i in range(n)]


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/wSJV1A/view/fnQ2Ve/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。