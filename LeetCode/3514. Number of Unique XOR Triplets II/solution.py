class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums = list(set(nums))  # 优化：去重，减少循环次数
        st = {x ^ y for x, y in combinations(nums, 2)} | {0}
        return len({xy ^ z for xy in st for z in nums})

作者：灵茶山艾府
链接：https://leetcode.cn/problems/number-of-unique-xor-triplets-ii/solutions/3649377/mei-ju-fu-oulogu-fwt-zuo-fa-pythonjavacg-69r3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。