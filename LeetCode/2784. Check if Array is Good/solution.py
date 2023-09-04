class Solution:

    def isGood(self, nums: List[int]) -> bool:

        n = len(nums) - 1

        cnt = Counter(nums)

        return cnt[n] == 2 and all(cnt[i] == 1 for i in range(1, n))

作者：灵茶山艾府
链接：https://leetcode.cn/problems/check-if-array-is-good/solutions/2354992/on-yi-ci-bian-li-by-endlesscheng-rdpp/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)-1
        if nums[-1] != n: return False
        for i in range(n):
            if nums[i] != i+1:
                return False
        return True