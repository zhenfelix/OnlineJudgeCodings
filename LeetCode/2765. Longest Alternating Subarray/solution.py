class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n-1):
            if nums[i+1] != nums[i]+1:
                continue
            for j in range(i+1,n):
                if nums[j] != nums[i+(j-i)%2]:
                    break
                ans = max(ans,j-i+1)
        return ans 


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i + 1] - nums[i] != 1:
                i += 1
                continue
            i0 = i
            i += 1
            while i < n and nums[i] == nums[i0] + (i - i0) % 2:
                i += 1
            ans = max(ans, i - i0)
            i -= 1
        return ans


作者：endlesscheng
链接：https://leetcode.cn/problems/longest-alternating-subarray/solution/on-fen-zu-xun-huan-by-endlesscheng-bbws/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。