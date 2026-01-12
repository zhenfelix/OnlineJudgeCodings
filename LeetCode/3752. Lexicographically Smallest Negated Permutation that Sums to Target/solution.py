class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        mx = n * (n + 1) // 2
        if abs(target) > mx or (mx - target) % 2:
            return []
        neg_s = (mx - target) // 2  # 取负号的元素（的绝对值）之和

        ans = [0] * n
        l, r = 0, n - 1
        # 从 1,2,...,n 中选一些数，元素和等于 neg
        # 为了让负数部分的字典序尽量小，从大往小选
        for x in range(n, 0, -1):
            if neg_s >= x:
                neg_s -= x
                ans[l] = -x
                l += 1
            else:
                # 大的正数填在末尾
                ans[r] = x
                r -= 1
        return ans

作者：灵茶山艾府
链接：https://leetcode.cn/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/solutions/3839568/tan-xin-on-zuo-fa-pythonjavacgo-by-endle-7ojw/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。