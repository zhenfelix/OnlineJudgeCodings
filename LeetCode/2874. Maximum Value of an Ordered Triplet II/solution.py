class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = inf
        mx = [-inf]*n 
        mi = [inf]*n 
        px, pi = -inf, inf 
        for i, v in enumerate(nums):
            mx[i] = max(mx[i],mx[i-1])
            mx[i] = max(mx[i],v-pi)
            mi[i] = min(mi[i],mi[i-1])
            mi[i] = min(mi[i],v-px)
            pi = min(pi,v)
            px = max(px,v)
            if i > 1:
                ans = min(ans, v*mx[i-1])
                ans = min(ans, v*mi[i-1])
        return -min(0,ans)


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf_max = [0] * (n + 1)
        for i in range(n - 1, 1, -1):
            suf_max[i] = max(suf_max[i + 1], nums[i])
        ans = pre_max = 0
        for j, x in enumerate(nums):
            ans = max(ans, (pre_max - x) * suf_max[j + 1])
            pre_max = max(pre_max, x)
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/9idUqp/view/QFZ1w1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。