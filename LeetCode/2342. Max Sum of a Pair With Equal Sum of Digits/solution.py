class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        mx = defaultdict(int)
        for num in nums:
            # s = sum(int(d) for d in str(num))
            s, x = 0, num
            while x:
                s += x % 10
                x //= 10
            if s in mx: ans = max(ans, mx[s] + num)
            mx[s] = max(mx[s], num)
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/solution/ha-xi-biao-wei-hu-zui-da-de-liang-ge-by-3ou64/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def calc(x):
            s = 0
            while x:
                s += x%10
                x //= 10
            return s
        mp = defaultdict(list)
        for x in nums:
            mp[calc(x)].append(x)
        ans = -1
        for k, v in mp.items():
            if len(v) > 1:
                v.sort()
                ans = max(ans, v[-1]+v[-2])
        return ans 