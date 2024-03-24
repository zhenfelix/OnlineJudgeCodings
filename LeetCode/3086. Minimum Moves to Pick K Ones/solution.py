class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxi: int) -> int:
        acc = list(accumulate(nums, initial=0))
        n = len(nums)
        pos_sum = list(accumulate((i if nums[i] else 0 for i in range(n)), initial=0))
        
        res = inf
        for i in range(n):
            ans = 0
            tmp = k
            for p in range(i - 1, i + 2):
                if 0 <= p < n and nums[p] and tmp:
                    tmp -= 1
                    ans += abs(p - i)
            if maxi >= tmp:
                res = min(res, ans + tmp * 2)
            else:
                ans = 2 * maxi
                tmp = k - maxi
                l, r = 0, n
                while l <= r:
                    m = (l + r) // 2
                    if acc[min(n, i + m + 1)] - acc[max(0, i - m)] >= tmp:
                        r = m - 1
                    else:
                        l = m + 1
                m = l
                ans += (pos_sum[min(n, i+m+1)] - pos_sum[i]) - (acc[min(n, i+m+1)] - acc[i]) * i
                ans += -(pos_sum[i+1] - pos_sum[max(0, i-m)]) + (acc[i+1] - acc[max(0, i-m)]) * i
                if acc[min(n, i + m + 1)] - acc[max(0, i - m)] > tmp:
                    ans -= m
                res = min(ans, res)
        return res


# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/xjZslE/view/69Zo9I/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。