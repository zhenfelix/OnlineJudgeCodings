class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        seen = [False]*51
        for a, b in ranges:
            for i in range(a, b+1):
                seen[i] = True
        for i in range(left,right+1):
            if not seen[i]:
                return False
        return True


class Solution:
    def isCovered(self, ranges, left, right):
        return all(any(l <= i <= r for l, r in ranges) for i in range(left, right + 1))        