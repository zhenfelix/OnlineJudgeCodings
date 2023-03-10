class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        arr = []
        n = len(weights)
        for i in range(n-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        k -= 1
        return sum(arr[-k:])-sum(arr[:k])