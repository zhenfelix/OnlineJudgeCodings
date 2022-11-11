class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n, s = 1, 0
        while True:
            s += n 
            if s == target or (s > target and (s-target)%2 == 0):
                break
            n += 1
        return n 