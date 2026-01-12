max = lambda a, b: b if b > a else a  # 手写 max 更快

class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            lowbit_min = inf
            lowbit_cnt = g = 0
            for j in range(i, -1, -1):
                x = nums[j]
                lb = x & -x
                if lb < lowbit_min:
                    lowbit_min, lowbit_cnt = lb, 1
                elif lb == lowbit_min:
                    lowbit_cnt += 1

                g = gcd(g, x)
                new_g = g * 2 if lowbit_cnt <= k else g
                ans = max(ans, new_g * (i - j + 1))
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/maximize-subarray-gcd-score/solutions/3695642/liang-chong-xie-fa-bao-li-mei-ju-logtric-zz7e/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。