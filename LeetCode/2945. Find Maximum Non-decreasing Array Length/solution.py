class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))
        f = [0] * (n + 1)
        last = [0] * (n + 1)
        q = deque([0])
        for i in range(1, n + 1):
            # 1. 去掉队首无用数据（计算转移时，直接取队首）
            while len(q) > 1 and s[q[1]] + last[q[1]] <= s[i]:
                q.popleft()
            
            # 2. 计算转移
            f[i] = f[q[0]] + 1
            last[i] = s[i] - s[q[0]]
            
            # 3. 去掉队尾无用数据
            while q and s[q[-1]] + last[q[-1]] >= s[i] + last[i]:
                q.pop()
            q.append(i)
        return f[n]

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/find-maximum-non-decreasing-array-length/solutions/2542102/dan-diao-dui-lie-you-hua-dp-by-endlessch-j5qd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# class Solution:
#     def findMaximumLength(self, A: List[int]) -> int:
#         n = len(A)
#         last = [0] + [inf] * n
#         acc = [0]
#         dp = [0] + [0] * n
#         for j in range(n):
#             a = A[j]
#             acc.append(a + acc[-1])
#             i = j
#             while last[i] > acc[-1] - acc[i]:
#                 i -= 1
#             last[j + 1] = acc[-1] - acc[i]
#             dp[j + 1] = dp[i] + 1
#         return dp[-1]


    def findMaximumLength(self, A: List[int]) -> int:
        n = len(A)
        acc = list(accumulate(A, initial = 0))
        pre = [0] * (n + 2)
        dp = [0] * (n + 1)
        i = 0
        for j,a in enumerate(A, 1):
            i = max(i, pre[j])
            dp[j] = dp[i] + 1
            k = bisect_left(acc, acc[j] * 2 - acc[i])
            pre[k] = j
        return dp[n]