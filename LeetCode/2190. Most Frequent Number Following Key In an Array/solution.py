class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        cc = Counter()
        for i in range(n-1):
            if nums[i] == key:
                cc[nums[i+1]] += 1
        res, cnt = 0, 0
        for k, v in cc.items():
            if v > cnt:
                res = k 
                cnt = v
        return res


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        return collections.Counter([nums[i] for i in range(1, len(nums)) if nums[i - 1] == key]).most_common(1)[0][0]


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/9WhoB7/view/s15EHo/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。