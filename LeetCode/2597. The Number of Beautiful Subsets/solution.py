# 我们也可以使用动态规划解题，先根据模 kk 的余数分类，接下来可以发现我们在对应类下不能连续取两个整数。这个可以直接使用前缀和减去最后一项得到。时间复杂度为 O(n+m)O(n+m). 如果 numsnums 范围较大，可以先排序，跳过中间那些不必要的计数为 00 的点，也是很容易优化的。

# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/4MTE6Z/view/3GJ3rW/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
powers = [1]
for _ in range(20):
    powers.append(powers[-1] * 2)

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        tmp = [[0] * (1000 // k + 1) for _ in range(k)]
        for num in nums:
            tmp[num % k][num // k] += 1

        ans = 1
        for item in tmp:
            acc = 1
            last = 0
            for count in item:
                last = (acc - last) * (powers[count] - 1)
                acc += last
            ans *= acc
        return ans - 1


# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/4MTE6Z/view/3GJ3rW/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
cnt = [0] * 2001 # nums[idx]-k 变为负数也不怕！
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        def dfs(idx):
            nonlocal ans
            if idx == n: ans += 1; return
            dfs(idx+1)
            # 查看距离为 k 是否有数存在
            if cnt[nums[idx] + k] == 0 and cnt[nums[idx] - k] == 0:
                cnt[nums[idx]] += 1
                dfs(idx+1)
                cnt[nums[idx]] -= 1
        dfs(0)
        return ans - 1 # 减去空集


# 作者：小羊肖恩
# 链接：https://leetcode.cn/circle/discuss/4MTE6Z/view/3GJ3rW/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        mp = dict()
        for i in range(n)[::-1]:
            s = 0
            for j in range(i+1,n):
                if nums[j]-nums[i] == k:
                    s |= (1<<j)
            mp[1<<i] = s 
        dp = [0]*(1<<n)
        dp[0] = 1
        for s in range(1,1<<n):
            flag = True
            if dp[s-(s&-s)] and not (mp[s&-s]&(s-(s&-s))):
                dp[s] = 1
        return sum(dp)-1 
