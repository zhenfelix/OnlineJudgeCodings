K = 5

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(K):
            s = False
            for num in nums:
                if num & (1 << i) > 0:
                    s = True
                    break
            if s:
                ans += 1 << (i + n - 1)
        return ans


# 作者：吴自华
# 链接：https://leetcode-cn.com/circle/discuss/COaQbh/view/z7mqn9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0]
        def dfs(i, cur):
            if i == n:
                res[0] += cur
                return
            dfs(i+1, cur)
            dfs(i+1, cur^nums[i])
            return
        dfs(0,0)
        return res[0]