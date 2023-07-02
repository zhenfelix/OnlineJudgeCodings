class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cur = 0
            cc = [0]*(n+10)
            mi = inf 
            mx = -inf
            for j in range(i,n):
                a = nums[j]
                mi = min(mi,a)
                mx = max(mx,a)
                cc[a] += 1
                if cc[a] <= 1: 
                    if a > mi and a < mx: cur -= 1 
                    if a > mi and cc[a-1] == 0: cur += 1
                    if a < mx and cc[a+1] == 0: cur += 1
                ans += cur
                # print(nums[i:j+1],cur,cc)
        return ans 

class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        right = [0] * n  # nums[i] 右侧的 x 和 x-1 的最近下标（不存在时为 n）
        idx = [n] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = nums[i]
            right[i] = min(idx[x], idx[x - 1])
            idx[x] = i

        ans = 0
        idx = [-1] * (n + 1)
        for i, (x, r) in enumerate(zip(nums, right)):
            # 统计 x 能产生多少贡献
            ans += (i - idx[x - 1]) * (r - i)  # 子数组左端点个数 * 子数组右端点个数
            idx[x] = i
        # 上面计算的时候，每个子数组的最小值必然可以作为贡献，而这是不合法的
        # 所以每个子数组都多算了 1 个不合法的贡献
        return ans - n * (n + 1) // 2


作者：endlesscheng
链接：https://leetcode.cn/problems/sum-of-imbalance-numbers-of-all-subarrays/solution/bao-li-mei-ju-pythonjavacgo-by-endlessch-2r7p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。