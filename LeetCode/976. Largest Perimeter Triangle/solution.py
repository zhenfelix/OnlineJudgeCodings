class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        arr = sorted(A, reverse=True)
        for i, a in enumerate(arr):
            if i<len(arr)-2 and arr[i+1]+arr[i+2]>a:
                return a+arr[i+1]+arr[i+2]
        return 0