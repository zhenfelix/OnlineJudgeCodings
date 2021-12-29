class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        presums, res = 0, -float('inf')
        q = [(0,-1)]
        for i in range(n*2):
            cur = nums[i%n]
            while i-q[0][1] > n:
                heapq.heappop(q)
            presums += cur
            res = max(res, presums-q[0][0])
            heapq.heappush(q,(presums,i))
        return res


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        presums, res = 0, -float('inf')
        q = deque([(0,-1)])
        for i in range(n*2):
            cur = nums[i%n]
            if i-q[0][1] > n:
                q.popleft()
            presums += cur
            res = max(res, presums-q[0][0])
            while q and q[-1][0] > presums:
                q.pop()
            q.append((presums,i))
        return res


class Solution:
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum


# 作者：xing-you-ji
# 链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray/solution/wo-hua-yi-bian-jiu-kan-dong-de-ti-jie-ni-892u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。