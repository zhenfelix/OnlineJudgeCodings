class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        m = min(nums)
        for x in nums:
            if x % m:
                return 1
        return (nums.count(m) + 1) // 2

作者：灵茶山艾府
链接：https://leetcode.cn/problems/minimize-length-of-array-using-operations/solutions/2613059/on-nao-jin-ji-zhuan-wan-pythonjavacgo-by-2lea/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。