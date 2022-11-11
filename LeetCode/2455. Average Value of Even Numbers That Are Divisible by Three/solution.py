class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = []
        for x in nums:
            if x%6 == 0:
                ans.append(x)
        return sum(ans)//len(ans) if ans else 0