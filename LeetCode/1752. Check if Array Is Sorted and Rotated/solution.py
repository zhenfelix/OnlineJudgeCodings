class Solution:
    def check(self, A):
        return sum(a > b for a, b in zip(A, A[1:] + A[:1])) <= 1        