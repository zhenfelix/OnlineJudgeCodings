class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odd, even = 0, 0
        for x in chips:
            if x & 1 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)