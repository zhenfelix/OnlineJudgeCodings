class Solution:
    def sumOfUnique(self, A):
        return sum(a for a, c in collections.Counter(A).items() if c == 1)        