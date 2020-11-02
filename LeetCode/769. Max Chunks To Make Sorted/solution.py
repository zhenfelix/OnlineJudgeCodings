class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res, reach = 0, -1
        for i, a in enumerate(arr):
            if i > reach:
                res += 1
            reach = max(reach,a)
        return res 