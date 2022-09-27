class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = left = or_ = 0
        for right, x in enumerate(nums):
            while or_ & x:
                or_ ^= nums[left]
                left += 1
            or_ |= x
            ans = max(ans, right - left + 1)
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-nice-subarray/solution/bao-li-mei-ju-pythonjavacgo-by-endlessch-z6t6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        for i, or_ in enumerate(nums):
            j = i - 1
            while j >= 0 and (or_ & nums[j]) == 0:
                or_ |= nums[j]
                j -= 1
            ans = max(ans, i - j)
        return ans


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-nice-subarray/solution/bao-li-mei-ju-pythonjavacgo-by-endlessch-z6t6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def calc(arr):
            Nmax = 32
            n = len(arr)
            pos = [-1]*Nmax
            reach = [-1]*n 
            for i, a in enumerate(arr):
                for j in range(Nmax):
                    bit = (a>>j)&1
                    if bit:
                        reach[i] = max(reach[i],pos[j])
                        pos[j] = i 
                reach[i] = max(reach[i-1],reach[i])
                # print(pos,reach[i])
            return [i-r for i, r in enumerate(reach)]

        
        return max(calc(nums)) 