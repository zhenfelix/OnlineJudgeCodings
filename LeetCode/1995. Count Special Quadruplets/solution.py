from collections import Counter

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        single = Counter()
        double = Counter()
        triple = Counter()
        ans = 0
        for num in nums:
            ans += triple[num]
            for d in double:
                triple[d + num] += double[d]
            for s in single:
                double[s + num] += single[s]
            single[num] += 1
        return ans


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/ktLQXn/view/6ghYtr/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cc = Counter(nums[2:])
        n = len(nums)
        res = 0
        for k in range(2,n):
            cc[nums[k]] -= 1
            for j in range(k):
                for i in range(j):
                    res += cc[nums[i]+nums[j]+nums[k]]
        return res