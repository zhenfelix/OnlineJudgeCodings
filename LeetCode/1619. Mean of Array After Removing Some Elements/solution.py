class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        delta = n//20
        return sum(arr[delta:-delta])/(n-delta*2)