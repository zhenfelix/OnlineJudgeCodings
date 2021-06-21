class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        for a, b, c in triplets:
            x, y, z = target
            if a <= x and b <= y and c <= z:
                p, q, w = cur
                cur = [max(a,p), max(b,q), max(c,w)]
        return cur == target
