class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n, m = len(arr1), len(arr2)
        return sum(all(abs(arr1[i]-arr2[j]) > d for j in range(m)) for i in range(n))