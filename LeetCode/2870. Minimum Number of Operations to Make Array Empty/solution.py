class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for v in cnt.values():
            if v == 1: return -1
            ans += (v + 2) // 3
        return ans


作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/slLdgm/view/ytByYQ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。