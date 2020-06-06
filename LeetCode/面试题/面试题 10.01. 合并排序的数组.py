class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1
        while i >= 0 or j >= 0:
            if j < 0 or (i >= 0 and A[i] > B[j]):
                A[k] = A[i]
                i -= 1
            elif i < 0 or A[i] <= B[j]:
                A[k] = B[j]
                j -= 1
            k -= 1
        return
