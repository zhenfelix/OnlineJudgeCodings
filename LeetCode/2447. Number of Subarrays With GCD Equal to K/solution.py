class Solution:

    def subarrayGCD(self, nums: List[int], k: int) -> int:

        ans = 0

        a = []  # [GCD，相同 GCD 区间的右端点]

        i0 = -1

        for i, x in enumerate(nums):

            if x % k:  # 保证后续求的 GCD 都是 k 的倍数

                a = []

                i0 = i

                continue

            a.append([x, i])

            # 原地去重，因为相同的 GCD 都相邻在一起

            j = 0

            for p in a:

                p[0] = gcd(p[0], x)

                if a[j][0] != p[0]:

                    j += 1

                    a[j] = p

                else:

                    a[j][1] = p[1]

            del a[j + 1:]

            if a[0][0] == k:  # a[0][0] >= k

                ans += a[0][1] - i0

        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/number-of-subarrays-with-gcd-equal-to-k/solutions/1917454/by-endlesscheng-1f1r/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        for i in range(n):
            g = nums[i]
            for j in range(i,n):
                g = gcd(g, nums[j])
                if g == k:
                    res += 1

        return res 