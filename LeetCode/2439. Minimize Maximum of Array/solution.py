class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((s + i - 1) // i for i, s in enumerate(accumulate(nums), 1))


作者：endlesscheng
链接：https://leetcode.cn/problems/minimize-maximum-of-array/solution/liang-chong-zuo-fa-er-fen-da-an-fen-lei-qhee6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = s = mx = nums[0]
        cnt = 1
        for x in nums[1:]:
            cnt += 1
            s += x
            if x > mx:
                mx = (s+cnt-1)//cnt
                ans = max(mx,ans)
        return ans

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def check(limit: int) -> bool:
            extra = 0
            for i in range(len(nums) - 1, 0, -1):
                extra = max(nums[i] + extra - limit, 0)
            return nums[0] + extra <= limit
        return bisect_left(range(max(nums)), True, key=check)


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/minimize-maximum-of-array/solution/liang-chong-zuo-fa-er-fen-da-an-fen-lei-qhee6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        lo, hi = 0, max(nums)
        n = len(nums)

        def check(t):
            arr = nums.copy()
            for i in range(1,n)[::-1]:
                if arr[i] > t:
                    delta = arr[i]-t
                    arr[i-1] += delta
            return arr[0] <= t 

        while lo <= hi:
            mid = (lo+hi)//2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo