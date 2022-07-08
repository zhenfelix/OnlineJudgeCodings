# https://codeforces.com/blog/entry/47821
class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            """变为不减数组的最小操作次数"""
            res, pq = 0, []  # 大根堆
            for num in nums:
                if not pq:
                    heappush(pq, -num)
                else:
                    preMax = -pq[0]
                    if preMax > num:
                        res += preMax - num
                        heappushpop(pq, -num)
                    heappush(pq, -num)
            return res

        return min(helper(nums), helper(nums[::-1]))


# 作者：981377660LMT
# 链接：https://leetcode.cn/problems/make-array-non-decreasing-or-non-increasing/solution/python-by-981377660lmt-g31k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def helper(nums: List[int]) -> int:
            """变为不减数组的最小操作次数

            取得最小的操作次数时，数组末尾元素必须等于原数组中的某个元素
            """
            n = len(nums)
            allNums = sorted(set(nums))
            m = len(allNums)

            dp = [[int(1e20)] * m for _ in range(n)]
            for j in range((m)):
                dp[0][j] = abs(nums[0] - allNums[j])
            for i in range(1, n):
                preMin = int(1e20)
                for j in range(m):
                    preMin = min(preMin, dp[i - 1][j])
                    dp[i][j] = preMin + abs(nums[i] - allNums[j])

            return min(dp[-1])

        return min(helper(nums), helper(nums[::-1]))


# 作者：981377660LMT
# 链接：https://leetcode.cn/problems/make-array-non-decreasing-or-non-increasing/solution/python-by-981377660lmt-g31k/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def convertArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')
        dp = [0]*1001
        for x in nums:
            ndp = [0]*1001
            pre = float('inf')
            for i in range(1001):
                pre = min(pre, dp[i])
                ndp[i] = pre+abs(i-x)
            dp = ndp
        ans = min(ans, min(dp))
        dp = [0]*1001
        for x in nums:
            ndp = [0]*1001
            pre = float('inf')
            for i in range(1001)[::-1]:
                pre = min(pre, dp[i])
                ndp[i] = pre+abs(i-x)
            dp = ndp
        ans = min(ans, min(dp))
        return ans

