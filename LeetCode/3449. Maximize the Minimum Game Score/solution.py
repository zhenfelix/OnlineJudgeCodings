class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def check(low: int) -> bool:
            n = len(points)
            rem = m
            pre = 0
            for i, p in enumerate(points):
                k = (low - 1) // p + 1 - pre  # 还需要操作的次数
                if i == n - 1 and k <= 0:  # 最后一个数已经满足要求
                    break
                if k < 1:
                    k = 1  # 至少要走 1 步
                rem -= k * 2 - 1  # 左右横跳
                if rem < 0:
                    return False
                pre = k - 1  # 右边那个数顺带操作了 k-1 次
            return True

        left = 1
        right = m*min(points)
        while left <= right:
            mid = (left + right) // 2
            # print(mid,check(mid))
            if check(mid):
                left = mid+1
            else:
                right = mid-1
        return right

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/maximize-the-minimum-game-score/solutions/3068672/er-fen-da-an-cong-zuo-dao-you-tan-xin-py-3bhl/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。