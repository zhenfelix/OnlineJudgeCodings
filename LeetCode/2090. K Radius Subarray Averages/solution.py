class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1]*n 
        presums = [0]
        for x in nums:
            presums.append(presums[-1]+x)
        for i, x in enumerate(nums):
            if i-k >= 0 and i+k < n:
                res[i] = (presums[i+k+1]-presums[i-k])//(k*2+1)
        return res



class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s = 0
        ans = [-1] * n
        for i in range(n):
            s += nums[i]
            if i >= 2 * k:
                ans[i - k] = s // (2 * k + 1)
                s -= nums[i - k * 2]
        return ans


作者：吴自华
链接：https://leetcode-cn.com/circle/discuss/S0NvzF/view/w3E3WF/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。