# 手写 min 更快
min = lambda a, b: b if b < a else a

class Solution:
    def minArraySum(self, nums: list[int], k: int) -> int:
        min_f = [inf] * k
        min_f[0] = 0  # s[0] = 0，对应的 f[0] = 0
        f = s = 0
        for x in nums:
            s = (s + x) % k
            # 不删除 x，那么转移来源为 f + x
            # 删除以 x 结尾的子数组，问题变成剩余前缀的最小和
            # 其中剩余前缀的元素和模 k 等于 s，对应的 f 值的最小值记录在 min_f[s] 中
            f = min(f + x, min_f[s])
            # 维护前缀和 s 对应的最小和，由于上面计算了 min，这里无需再计算 min
            min_f[s] = f
        return f

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-sum-after-divisible-sum-deletions/solutions/3755268/dong-tai-gui-hua-qian-zhui-he-pythonjava-nia8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 手写 min 更快
min = lambda a, b: b if b < a else a

class Solution:
    def minArraySum(self, nums: list[int], k: int) -> int:
        min_f = defaultdict(lambda: inf)
        min_f[0] = 0  # s[0] = 0，对应的 f[0] = 0
        f = s = 0
        for x in nums:
            s = (s + x) % k
            # 不删除 x，那么转移来源为 f + x
            # 删除以 x 结尾的子数组，问题变成剩余前缀的最小和
            # 其中剩余前缀的元素和模 k 等于 s，对应的 f 值的最小值记录在 min_f[s] 中
            f = min(f + x, min_f[s])
            # 维护前缀和 s 对应的最小和，由于上面计算了 min，这里无需再计算 min
            min_f[s] = f
        return f

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimum-sum-after-divisible-sum-deletions/solutions/3755268/dong-tai-gui-hua-qian-zhui-he-pythonjava-nia8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        mp = {0:-1}
        n = len(nums)
        nums.append(0)
        dp = [0]*(n+1)
        tot = sum(nums)
        for i in range(n):
            if i:
                nums[i] += nums[i-1]
                dp[i] = dp[i-1]
            s = nums[i]%k 
            if s in mp:
                j = mp[s]
                dp[i] = max(dp[i],dp[j]+nums[i]-nums[j])
            mp[s] = i 
        # print(nums,dp)
        return tot-dp[n-1]