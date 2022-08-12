class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        cnt = 0
        s = set()
        for cur in rolls:
            s.add(cur)
            if len(s) == k:
                s = set()
                cnt += 1
        return cnt+1