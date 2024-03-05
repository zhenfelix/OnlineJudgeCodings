class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        ans = cnt_mx = left = 0
        for x in nums:
            if x == mx:
                cnt_mx += 1
            while cnt_mx == k:
                if nums[left] == mx:
                    cnt_mx -= 1
                left += 1
            ans += left
        return ans


作者：灵茶山艾府
链接：https://leetcode.cn/circle/discuss/3ml97X/view/0Qg6pZ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)
        ans = 0
        j = cnt = 0
        for i in range(n):
            if nums[i] == mx:
                cnt += 1
            while cnt >= k:
                if nums[j] == mx:
                    cnt -= 1
                j += 1
            if cnt == k-1 and j-1 >= 0 and nums[j-1] == mx:
                ans += j
        return ans 